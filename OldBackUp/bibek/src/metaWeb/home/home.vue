<template>
  <div>
    <Header />
    <Landing />
    <HowItWorks />
    <OurTeam />
    <Contact/>
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
export default {
  components: {
    Header,
    Contact,
    OurTeam,
    HowItWorks,
    Landing,
    Footer
  }
};
</script>