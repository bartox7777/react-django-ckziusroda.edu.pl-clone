import React, { useEffect, Fragment } from "react";
import { useSelector } from "react-redux";
import { useAlert } from "react-alert";

const Alerts = () => {
  const alerts = useSelector((state) => state.alerts);
  const _alert = useAlert();

  useEffect(() => {
    if (alerts.length > 0) {
      alerts.map((alert) => {
        if (alert.type === "error") {
          if (alert.msg.username) {
            alert.msg.username.map((alert_username) => {
              _alert.error(`Nazwa użytkownika: ${alert_username}`);
            });
          }
          if (alert.msg.password) {
            alert.msg.username.map((alert_password) => {
              _alert.error(`Hasło: ${alert_password}`);
            });
          }
          if (alert.msg.non_field_errors) {
            _alert.error("Niepoprawne dane logowania");
          }
        }
      });
    }
  }, [alerts]);

  return <Fragment />;
};

export default Alerts;
