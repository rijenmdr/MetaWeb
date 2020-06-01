import axios from "axios";
const state = {
  token: "",
  error: false,
  user: "",
};
const mutations = {
  SET_TOKEN(state, token) {
    state.token = token;
  },
  SET_ERROR(state, bol) {
    state.error = bol;
  },
  SET_USER(state, user) {
    state.user = user.username;
  },
  LOGOUT(state) {
    state.token = null;
  },
};
const actions = {
  async Login({ commit, dispatch }, credential) {
    
    commit("SET_ERROR", false);
    await axios
      .post("http://localhost:8000/rest-auth/login/", {
        username: credential.username,
        password: credential.password,
      })
      .then((res) => {
        commit("SET_USER", credential);
        commit("SET_TOKEN", res.data.key);
        if (credential.remember) {
          localStorage.setItem("token", res.data.key);
          const now = new Date();
          const expirationDate = new Date(now.getTime() + 3600000);
          localStorage.setItem("expiresIn", expirationDate);
          localStorage.setItem("user", credential.username);
        }
        dispatch("addNotifications", {
          type: "success",
          message: "login in successful",
        });
      })
      .catch((err) => {
        commit("SET_ERROR", true);
      });
  },
  async signUp({ commit,dispatch }, data) {
    console.log(data)
    commit("SET_ERROR", false);
    await axios
      .post("http://localhost:8000/registration/", {
        username: data.username,
        email: data.email,
        password1: data.password1,
        password2: data.password2,
      })
      .then((res) => {
        console.log(res);
        const now = new Date();
        const expirationDate = new Date(now.getTime() + 3600000);
        localStorage.setItem("expiresIn", expirationDate);
        localStorage.setItem("token", res.data.key);
        commit("SET_TOKEN", res.data.key);
        localStorage.setItem("user", data.username);
        commit("SET_TOKEN", res.data.key);
        dispatch("addNotifications", {
          type: "success",
          message: "SignUp in successful",
        });
      })
      .catch((err) => {
        console.log(err);
        console.log("error aayo");
        commit("SET_ERROR", true);
      });
  },
  logout({ commit,dispatch }) {
    localStorage.removeItem("token");
    localStorage.removeItem("expiresIn");
    commit("LOGOUT");
    dispatch("addNotifications", {
      type: "danger",
      message: "You are now logged out",
    });
  },
};
const getters = {
  getToken: (state) => {
    return state.token;
  },
  getError: (state) => {
    return state.error;
  },
  getUser: (state) => {
    return state.user;
  },
};
export default {
  state,
  getters,
  mutations,
  actions,
};
