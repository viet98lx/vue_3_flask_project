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
import Repository from "../repositories/RepositoryFactory"
const ActorRepository = Repository.get("actors")

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
    async getActorData() {
      console.log("call get actors")
      const resp = await ActorRepository.getActor(this.actor_id)
      this.actor = resp['data']
      console.log(this.actor.actor_id)
    },
    async deleteActor(){
      console.log("call get actors")
      await ActorRepository.delete(this.actor_id)
      this.$router.push({
            name:'actorshome'
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