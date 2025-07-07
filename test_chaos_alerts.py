from chaos_genius.controllers.alert_controller import get_alert_list


def main():
    # Get all alerts with channel 'email'
    email_alerts = get_alert_list(
        as_obj=True,
        extra_filters=[
            # Filter for email channel
            __import__("chaos_genius.databases.models.alert_model").databases.models.alert_model.Alert.alert_channel == "email"
        ],
    )
    print(f"Found {len(email_alerts)} email alerts.")

    # # Trigger each alert and print the result
    # for alert in email_alerts:
    #     print(f"Triggering alert: {alert.id} - {alert.alert_name}")
    #     try:
    #         result = check_and_trigger_alert(alert.id)
    #         print(f"Alert {alert.id} triggered: {result}")
    #     except Exception as e:
    #         print(f"Failed to trigger alert {alert.id}: {e}")


if __name__ == "__main__":
    main()
