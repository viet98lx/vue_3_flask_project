<template>
<!--<h1>this is home page</h1>-->
<div class="container mt-5">
  <div v-for="actor in actors" :key="actor.actor_id">
    <h3>
      <router-link class="link-style" :to="{name:'detail',params:{actor_id:actor.actor_id}}" v-text="actor.first_name+' '+actor.last_name"></router-link>
    </h3>
  </div>
</div>
</template>

<script>
export default {
  name: "Home",
  data(){
    return {
      actors: [],
    }
  },
  methods: {
    getActors() {
      // console.log("call get actors")
      fetch('http://127.0.0.1:5000/get', {
        method:"GET",
        headers: {
          "Content-Type":"application/json"
        }
      })
      .then(resp => resp.json())
      .then(data => {
        console.log(data)
        this.actors.push(...data)
      })
      .catch(error =>{
        console.log(error)
      })
    }
  },
  created(){
    this.getActors()
  }
}
</script>

<style scoped>
.link-style:hover{
  font-weight: bold;
  color: black;
  text-decoration: aqua;
}
</style>