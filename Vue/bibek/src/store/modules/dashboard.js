import axios from "axios";
const state = {
  webid: "",
};
const mutations = {
  SET_WEBID(state, id) {
    state.webid = id;
  },
};
const actions = {
  setId({ commit }, data) {
    commit("SET_WEBID", data);
  },
};
const getters = {
  getWebId: (state) => {
    return state.webid;
  },
};
export default {
  state,
  getters,
  mutations,
  actions,
};
