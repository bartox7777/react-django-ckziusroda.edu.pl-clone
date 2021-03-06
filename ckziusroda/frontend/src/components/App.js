import React, { useEffect } from "react";
import ReactDOM from "react-dom";

import { Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";

import { HashRouter as Router, Route, Switch } from "react-router-dom";

import { Provider } from "react-redux";
import store from "../store";

import Header from "./layout/Header";
import Footer from "./layout/Footer";
import Alerts from "./layout/Alerts";

import MainPage from "./main_page/MainPage";
import PostsByCategory from "./posts/PostsByCategory";
import PostBySlug from "./posts/PostBySlug";
import PostsByPhrase from "./posts/PostsByPhrase";
import PostsByDate from "./posts/PostsByDate";
import CreatePost from "./posts/CreatePost";

import AddCategory from "./categories/AddCategory";

import UploadFile from "./common/UploadFile";

import Login from "./authorization/Login";
import Logout from "./authorization/Logout";
import SecureRoute from "./authorization/SecureRoute";

import { loadUser } from "../actions/authentication";

import "react-calendar/dist/Calendar.css";
import "../styles/body.css";

const App = () => {
  useEffect(() => {
    store.dispatch(loadUser());
  }, []);

  const alertOptions = {
    position: "top center",
    timeout: 5000,
  };

  return (
    <Provider store={store}>
      <AlertProvider template={AlertTemplate} {...alertOptions}>
        <Router>
          <>
            <Alerts />
            <Header />
            <Switch>
              <Route exact path="/" component={MainPage} />
              <Route
                exact
                path="/posty/:category_slug/"
                component={PostsByCategory}
              />
              <Route
                exact
                path="/posty/:category_slug/:post_slug"
                component={PostBySlug}
              />
              <Route exact path="/szukaj/:phrase" component={PostsByPhrase} />
              <Route
                exact
                path="/archiwum/:year/:month"
                component={PostsByDate}
              />
              <Route exact path="/zaloguj" component={Login} />
              <SecureRoute exact path="/wyloguj" component={Logout} />
              <SecureRoute exact path="/dodaj-post" component={CreatePost} />
              <SecureRoute
                exact
                path="/dodaj-kategorie"
                component={AddCategory}
              />
              <SecureRoute exact path="/przeslij-plik" component={UploadFile} />
            </Switch>
            <Footer />
          </>
        </Router>
      </AlertProvider>
    </Provider>
  );
};

export default App;
ReactDOM.render(<App />, document.querySelector("#app"));
