import axios from "axios";
const state = {
  userPresent: "",
  paidUser: "",
  remainingDays: 0,
  alert: true,
};
//yesma alert chai as flag matrai use garayko kena vane everytime dashboard ma jada chai dateexpired call vaiderane raixa so flag use garayrw rokayko ho alert lay ..abo 30 days exceed vayo vane alert auxa 
const mutations = {
  SET_PAIDUSER(state) {
    state.userPresent = "present";
  },
  SET_DAYS(state, val) {
    state.remainingDays = val;
  },
  SET_ALERT(state) {
    state.alert =false;
  },
  REMOVE_PAIDUSER(state) {
    state.userPresent = "";
    state.paidUser = [];
  },
  ADD_PAIDUSER(state, val) {
    state.paidUser = val;
  },
};
const actions = {
  setPaidUser({ commit }, val) {
    commit("SET_PAIDUSER");
    commit("ADD_PAIDUSER", val);
  },
  removePaidUser({ commit }) {
    commit("REMOVE_PAIDUSER");
  },
  setRemainingDays({ commit }, val) {
    commit("SET_DAYS", val);
  },
  setAlert({ commit }) {
    commit("SET_ALERT");
  },
};
const getters = {
  getPaidUser: (state) => {
    return state.userPresent;
  },
  getPaidUserInfo: (state) => {
    return state.paidUser;
  },
  getRemainigDays: (state) => {
    return state.getRemainigDays;
  },
  getAlert: (state) => {
    return state.alert;
  },
};
export default {
  state,
  getters,
  mutations,
  actions,
};
