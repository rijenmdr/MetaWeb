import axios from "axios";
const state = {
  webid: "",
  userSite: [],
};
const mutations = {
  SET_WEBID(state, id) {
    state.webid = id;
  },
  SET_UserSite(state, val) {
    state.userSite = val;
  },
  UPDATE_SITE(state, val) {
    console.log("update hudai xa");
    console.log(val);
    state.userSite = "";
  },
};
const actions = {
  setId({ commit }, data) {
    commit("SET_WEBID", data);
  },
  async setUserSite({ commit }, data) {
   
    let JWTToken = data.token;
    await axios
      .post(
        "http://localhost:8000/api/dashboard",
        {
          user: data.user,
        },
        {
          headers: {
            Authorization: `Token ${JWTToken}`,
          },
        }
      )
      .then((res) => {
        commit("SET_UserSite", res.data.data);
      });
    
  },
  updateUserSite({ commit }, data) {
    commit("UPDATE_SITE", data);
  },
};
const getters = {
  getWebId: (state) => {
    return state.webid;
  },
  getUserSite: (state) => {
    return state.userSite;
  },
};
export default {
  state,
  getters,
  mutations,
  actions,
};
