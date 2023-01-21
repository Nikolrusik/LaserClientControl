import "./App.css";
import React from "react";
import axios from "axios";

class App extends React.Component {
  connstructor(props) {
    super(props);
    this.state = {
      clients: [],
      sessions: [],
      token: "",
    };
  }

  get_headers() {
    let headers = {
      "Content-Type": "application/json",
    };
    if (this.is_authenticated()) {
      headers["Autorization"] = "Token" + this.state.token;
    }
  }

  is_authenticated() {
    return this.state.token != "";
  }

  get_token(username, password) {
    axios
      .post("http://127.0.0.1:8000/api-token-auth/", {
        username: username,
        password: password,
      })
      .then((response) => {
        console.log(response.data);
        this.set_token(response.data["token"]);
      })
      .catch((error) => alert("Неверный логин или пароль"));
  }

  load_data() {
    const headers = this.get_headers();
  }

  render() {
    return (
      <div>
        <BrowserRouter>
          <Routes>
            <Route path="/login" element={<div></div>} />
            <Route path="/new_session/new_client" element={<div></div>} />
            <Route path="/new_session/active_client" element={<div></div>} />
            <Route path="/sessions" element={<div></div>} />
            <Route path="/not_comed" element={<div></div>} />
            <Route path="/all_clients" element={<div></div>} />
            <Route path="/birthdays" element={<div></div>} />
          </Routes>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
