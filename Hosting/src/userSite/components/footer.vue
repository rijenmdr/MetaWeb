<template>
  <footer
    id="main-footer"
    class="text-center text-white mt-5 p-5"
    :style="{backgroundColor:backgroundColor}"
  >
    <div class="container">
      <div class="row">
        <div class="col">
          <p class="lead">
            copyright &copy;
            <span id="year"></span>
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  props: ["backgroundColor"]
};
</script>
