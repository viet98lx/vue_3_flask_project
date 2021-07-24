<template>
<!--<h1>Create</h1>-->
  <div class="container mt-5">
    <form @submit.prevent="insertActor">
      <input type="text" class="form-control" placeholder="Please enter your first name" v-model="first_name"/>
      <br/>
      <textarea rows="1" class="form-control"
                placeholder="Please enter your last name"
                v-model="last_name"></textarea>
      <button class="btn btn-success mt-4">
        Publish information
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
  name: "Create",
  data(){
    return {
      first_name:null,
      last_name:null,
      error:null
    }
  },
  methods: {
    insertActor() {
      console.log("call insert actor")
      if (!this.first_name || !this.last_name) {
        this.error = "Please add all fields"
      } else {
        fetch('http://localhost:5000/add', {
          method: "POST",
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
  }
}
</script>

<style scoped>

</style>