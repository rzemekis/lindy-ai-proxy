from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)
WORKSPACE_DIR = os.getcwd()


@app.route('/rpc', methods=['POST'])
def handle_rpc():
    data = request.json
    action = data.get("action")
    params = data.get("params", {})

    if action == "create_file":
        filename = os.path.basename(params.get("filename"))
        content = params.get("content", "")
        filepath = os.path.join(WORKSPACE_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        # Logging into terminal
        print(f"\n[Lindy]   Created file: {filename} ({len(content)} byte)")
        return jsonify({"status": "success", "message": f"File {filename} created locally."})

    elif action == "read_file":
        filename = os.path.basename(params.get("filename"))
        filepath = os.path.join(WORKSPACE_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                return jsonify({"status": "success", "content": f.read()})
            return jsonify({"status": "error", "message": "404 File not found"})

    elif action == "execute_command":
        command = params.get("command")
        print(f"\n[Lindy]  Executing: {command}")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=15)
            return jsonify({
                "status": "success",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode
            })
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})

    elif action == "patch_file":
        filename = os.path.basename(params.get("filename"))
        find_text = params.get("find")
        replace_text = params.get("replace")
        filepath = os.path.join(WORKSPACE_DIR, filename)

        if not os.path.exists(filepath):
            return jsonify({"status": "error", "message": "File not found"})

        with open(filepath, "r", encoding="utf-8") as f:
            file_content = f.read()

        if find_text not in file_content:
            return jsonify({"status": "error", "message": "Original text block not found in file"})

        # Replace specific code block
        new_content = file_content.replace(find_text, replace_text)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        # Logging into terminal
        print(f"\n[Lindy] Patched file: {filename}")
        return jsonify({"status": "success", "message": f"File {filename} patched successfully."})

    return jsonify({"status": "error", "message": "Unknown action"})


if __name__ == '__main__':
    # Flask-logging is disabled
    import logging

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    print(" Local lindy-backend started on port 5000...")
    app.run(port=5000)