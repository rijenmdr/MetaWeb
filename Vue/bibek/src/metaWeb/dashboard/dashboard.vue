<template>
  <div>
    <Header />
    <Actions />
    <MainDash/>
    <Footer />
  </div>
</template>
<script>
import Header from "./header";
import Actions from "./actions";
import Footer from "../home/footer";
import MainDash from './mainDash'
export default {
  components: {
    Header,
    Footer,
    Actions,
    MainDash
  }
};
</script>