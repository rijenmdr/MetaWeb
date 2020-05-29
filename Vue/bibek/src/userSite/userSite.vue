<template>
  <div>
    <Header :nameOfSite="nameOfSiteH"/>
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
    />
  </div>
</template>
<script>
import axios from "axios";
import Header from "./components/header";
import Landing from "./components/landing";
import Features from "./components/features";
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
      user: ""
    };
  },
  components: {
    Header,
    Landing,
    Features
  },
  async created() {
    let JWTToken = "4338ce3d59ee2663bbaa9a5bd51bd97f2ec1edd1";
    let id = this.$route.params.id;
    
    await axios
      .get("http://localhost:8000/api/get_website/" + id, {
        headers: {
          Authorization: `Token ${JWTToken}`
        }
      })
      .then(res => {
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
      });
  }
};
</script>