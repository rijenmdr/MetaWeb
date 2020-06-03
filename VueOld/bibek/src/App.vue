<template>
  <div>
    <div>
      <router-view></router-view>
    </div>
    <NotificationList/>
  </div>
</template>
<script>
import NotificationList from "./components/notificationList";
export default {
  components: {
    NotificationList
  }
};
</script>
<style>
</style>
