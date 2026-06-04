import requests
import json
import sys

URL = "https://api.lindy.ai/graphql"
HEADERS = {
    "accept": "application/graphql-response+json; charset=utf-8, application/json; charset=utf-8",
    "content-type": "application/json",
    "origin": "https://chat.lindy.ai",
    "referer": "https://chat.lindy.ai/",
    "user-agent": "",
    "x-lindy-csrf-protection": "1",
}
#paste you own cookies here
COOKIES = {
    "lsid": "",
    "lindy_anon_id": "",
    "redirectToChat": "true"
}
#paste your active sub-task id here
SUB_TASK_ID = ""


def send_to_lindy(message):
    """Send user prompt to Lindy backend via GraphQL mutation"""
    graphql_query = """
    mutation useTaskInput_sendUserMessageToSubTaskMutation($input: SendUserMessageToSubTaskInput!) {
      sendUserMessageToSubTask(input: $input) {
        __typename
        ... on MutationSendUserMessageToSubTaskSuccess {
          data { subTask { status } }
        }
      }
    }
    """
    payload = {
        "query": graphql_query,
        "variables": {
            "input": {
                "subTaskId": SUB_TASK_ID,
                "message": message,
                "attachmentIds": [],
                "timeZone": "Europe/Moscow",
                "interactionPoint": "task_view",
                "sentAt": "2026-06-04T19:25:34.311Z",
                "modelOverride": None,
                "setAsDefaultModel": False
            }
        }
    }
    try:
        res = requests.post(URL, json=payload, headers=HEADERS, cookies=COOKIES)
        return res.status_code == 200
    except Exception as e:
        print(f"[Error] Failed to send: {e}")
        return False


def main():
    print("\nClaude-Lindy CLI Agent started.")
    print("Enter your tasks below (Press Ctrl+C to exit):\n")

    while True:
        try:
            user_input = input("Claude-Lindy > ")
            if not user_input.strip():
                continue

            print("Sending task to Lindy cloud...")
            success = send_to_lindy(user_input)

            if success:
                print("Task accepted by Lindy. Awaiting local execution...")
            else:
                print("[Error] Failed to deliver task.")

        except KeyboardInterrupt:
            print("\nExiting CLI.")
            sys.exit(0)


if __name__ == "__main__":
    main()
