<template>
  <div>
    <Header :nameOfSite="nameOfSiteH"/>
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
      user:''
    };
  },
  components: {
    Header,
    Landing,
    Features
  },
  created() {
    let JWTToken = "4338ce3d59ee2663bbaa9a5bd51bd97f2ec1edd1";
    // let id = this.$store.getters.getWebId;
    let id = 2;
    console.log(id);
    axios
      .get("http://localhost:8000/api/get_website/" + id, {
        headers: {
          Authorization: `Token ${JWTToken}`
        }
      })
      .then(res => {
        this.nameOfSiteH = res.data.website.nameOfSiteH
        this.headingOneH = res.data.website.headingOneH
        this.descriptionOneH = res.data.website.descriptionOneH
        this.headingTwoH = res.data.website.headingTwoH
        this.descriptionTwoH = res.data.website.descriptionTwoH
        this.headingThreeH = res.data.website.headingThreeH
        this.descriptionThreeH = res.data.website.descriptionThreeH
        this.featureOneH = res.data.website.featureOneH
        this.featureTwoH = res.data.website.featureTwoH
        this.featureThreeH = res.data.website.featureThreeH
        this.introductionA = res.data.website.introductionA
        this.whatWeDoA = res.data.website.whatWeDoA
        this.titleC = res.data.website.titleC
        this.emailC = res.data.website.emailC
        this.descriptionC = res.data.website.descriptionC
        this.phoneC = res.data.website.phoneC
        this.addressC = res.data.website.addressC
        this.user = res.data.website.user
        
      });
  }
};
</script>