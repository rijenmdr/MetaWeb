<template>
  <div>
    <Header :nameOfSite="nameOfSiteH" :backgroundColor="backgroundColor" />
    <Landing
      :headingOneH="headingOneH"
      :descriptionOneH="descriptionOneH"
      :headingTwoH="headingTwoH"
      :descriptionTwoH="descriptionTwoH"
      :headingThreeH="headingThreeH"
      :descriptionThreeH="descriptionThreeH"
      :featureOneH="featureOneH"
      :featureTwoH="featureTwoH"
      :featureThreeH="featureThreeH"
      :featureOneDesH="featureOneDesH"
      :featureTwoDesH="featureTwoDesH"
      :featureThreeDesH="featureThreeDesH"
    />
    <Footer :backgroundColor="backgroundColor" />
  </div>
</template>
<script>
import axios from "axios";
import Header from "./components/header";
import Landing from "./components/landing";
import Features from "./components/features";
import Footer from "./components/footer";
import host from '../host.js'
export default {
  data() {
    return {
      nameOfSiteH: "",
      headingOneH: "",
      descriptionOneH: "",
      headingTwoH: "",
      descriptionTwoH: "",
      headingThreeH: "",
      descriptionThreeH: "",
      featureOneH: "",
      featureTwoH: "",
      featureThreeH: "",
      introductionA: "",
      whatWeDoA: "",
      titleC: "",
      emailC: "",
      descriptionC: "",
      phoneC: "",
      addressC: "",
      user: "",
      featureOneDesH: "",
      featureTwoDesH: "",
      featureThreeDesH: "",
      backgroundColor: ""
    };
  },
  components: {
    Header,
    Landing,
    Features,
    Footer
  },
  async created() {
    let id = this.$route.params.id;

    await axios.get(host.host+"/api/get_website/" + id).then(res => {
      this.$store.dispatch("setWebsite", res.data.website);
      this.nameOfSiteH = res.data.website.nameOfSiteH;
      this.headingOneH = res.data.website.headingOneH;
      this.descriptionOneH = res.data.website.descriptionOneH;
      this.headingTwoH = res.data.website.headingTwoH;
      this.descriptionTwoH = res.data.website.descriptionTwoH;
      this.headingThreeH = res.data.website.headingThreeH;
      this.descriptionThreeH = res.data.website.descriptionThreeH;
      this.featureOneH = res.data.website.featureOneH;
      this.featureTwoH = res.data.website.featureTwoH;
      this.featureThreeH = res.data.website.featureThreeH;
      this.featureOneDesH = res.data.website.featureOneDesH;
      this.featureTwoDesH = res.data.website.featureTwoDesH;
      this.featureThreeDesH = res.data.website.featureThreeDesH;
      this.backgroundColor = res.data.website.backgroundColor;
    });
  }
};
</script>