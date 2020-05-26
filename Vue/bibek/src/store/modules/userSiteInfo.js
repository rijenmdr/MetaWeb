import axios from "axios";
const state = {
  website: "",
};
const mutations = {
  SET_WEBSITE(state, value) {
    state.website = value;
  },
};
const actions = {
  setWebsite({ commit }, data) {
    commit("SET_WEBSITE", data);
  },
};
const getters = {
  getWebsite: (state) => {
    return state.website;
  },
};
export default {
  state,
  getters,
  mutations,
  actions,
};
