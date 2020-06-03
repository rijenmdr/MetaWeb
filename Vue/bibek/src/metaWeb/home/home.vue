<template>
  <div>
    <Header />
    <Landing />
    <HowItWorks />
    <Premium />
    <OurTeam />
    <Contact />
    <Footer />
  </div>
</template>
<script>
import Header from "./header";
import Landing from "./landingView";
import HowItWorks from "./howItWorks";
import OurTeam from "./ourTeam";
import Contact from "./contactUs";
import Footer from "./footer";
import Premium from "./premium";
export default {
  components: {
    Header,
    Contact,
    OurTeam,
    HowItWorks,
    Landing,
    Footer,
    Premium
  }
};
</script>