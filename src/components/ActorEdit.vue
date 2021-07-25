<template>
  <div class="container mt-5">
    <form @submit.prevent="updateActor">
      <input type="text" class="form-control" placeholder="Please enter your first name" v-model="first_name"/>
      <br/>
      <textarea rows="1" class="form-control"
                placeholder="Please enter your last name"
                v-model="last_name"></textarea>
      <button class="btn btn-success mt-4">
        Update information
      </button>
    </form>
    <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5"
         role="alert">
      <strong>{{this.error}}</strong>
    </div>
  </div>
</template>

<script>
export default {
  name: "ActorEdit",
  props:{
    actor_id:{
      type:[Number,String],
      required:true
    }
  },
  methods:{
    updateActor(){
      console.log("call update actor")
      if (!this.first_name || !this.last_name) {
        this.error = "Please add all fields"
      } else {
        fetch(`http://localhost:5000/actor/update/${this.actor_id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({first_name:this.first_name,last_name:this.last_name})
        })
        .then(resp => resp.json())
        .then(data => {
          console.log(data)
          // this.actors.push(...data)
          // this.actor = data
          this.$router.push({
            name:'Home'
          })
        })
        .catch(error => {
          console.log(error)
        })
      }
    }
  },
  data(){
    return {
      first_name:null,
      last_name:null,
      error:null
    }
  },
  beforeRouteEnter(to, from, next){
    if(to.params.actor_id != undefined){
      fetch(`http://localhost:5000/actor/get/${to.params.actor_id}/`, {
        method:"GET",
        headers: {
          "Content-Type":"application/json",
        }
      })
      .then(resp => resp.json())
      .then(data => {
        console.log(data)
        // this.actors.push(...data)
        return next(vm => (vm.first_name=data.first_name, vm.last_name=data.last_name))
        // this.actor = data
      })
      .catch(error =>{
        console.log(error)
      })
    }
    else{
      return next()
    }
  }
}
</script>

<style scoped>

</style>