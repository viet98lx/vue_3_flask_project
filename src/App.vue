<template>
  <title>Vue & flask</title>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>

</template>

<script>

import Navbar from "@/components/Navbar";
// import Home from "@/components/Home";
export default {
  name: 'App',
  components: {
    Navbar
  },
  watch: {
        $route: {
            immediate: true,
            handler(to) {
                document.title = to.meta.title || 'Sakila demo';
            }
        },
    }
}
</script>

<style>
</style>
