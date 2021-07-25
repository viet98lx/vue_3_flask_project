<template>
<div class="container mt-5">
  <strong>ID:</strong><p>{{actor.actor_id}}</p>
  <strong>NAME:</strong><p>{{actor.first_name}} {{actor.last_name}}</p>
  <strong>LAST UPDATE TIME:</strong><p>{{actor.last_update}}</p>
  <button class="btn btn-danger mx-3 mt-3" @click="deleteActor">Delete</button>
  <router-link :to="{name:'actoredit', params:{actor_id:actor.actor_id}}"
  class="btn btn-success mt-3">Update</router-link>
</div>
</template>

<script>
export default {
  name: "ActorDetail",
  data(){
    return {
      actor:{}
    }
  },
  props: {
    actor_id: {
      type:[Number,String],
      required:true
    }
  },
  methods: {
    getActorData() {
      console.log("call get actors")
      fetch(`http://localhost:5000/actor/get/${this.actor_id}/`, {
        method:"GET",
        headers: {
          "Content-Type":"application/json",
        }
      })
      .then(resp => resp.json())
      .then(data => {
        console.log(data)
        // this.actors.push(...data)
        this.actor = data
      })
      .catch(error =>{
        console.log(error)
      })
    },
    deleteActor(){
      console.log("call get actors")
      fetch(`http://localhost:5000/actor/delete/${this.actor_id}/`, {
        method:"DELETE",
        headers: {
          "Content-Type":"application/json",
        }
      })
      .then(() => {
        // console.log(data)
        // this.actors.push(...data)
        // this.actor = data
        this.$router.push({name:'Home'})
      })
      .catch(error =>{
        console.log(error)
      })
    }
  },
  created() {
    this.getActorData()
  }
}
</script>

<style scoped>

</style>