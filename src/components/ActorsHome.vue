<template>
  <div class="offset mt-5">
    <router-link to="actor_create"
    class="btn btn-success mt-3">ADD ACTOR</router-link>
    <table class="table table-bordered">
    <thead>
      <tr>
        <th>ID</th>
        <th>FULL NAME</th>
        <th>LAST UPDATE</th>
        <th>SEE DETAIL</th>
      </tr>
    </thead>
    <tbody>
    <tr v-for="actor in displayedPosts" :key="actor.actor_id">
      <td style="text-align:center">{{actor.actor_id}}</td>
      <td>{{actor.full_name}}</td>
      <td>{{actor.last_update}}</td>
      <td><router-link class="link-style" :to="{name:'actor_detail',params:{actor_id:actor.actor_id}}">DETAIL</router-link></td>
    </tr>
    </tbody>
  </table>
  <nav aria-label="Page navigation example">
    <ul class="pagination">
<!--      <h1>Nav bar</h1>-->
      <li class="page-item">
        <button type="button" class="page-link" v-if="page != 1" @click="page--"> Previous </button>
      </li>
      <li class="page-item">
        <button type="button" class="page-link" v-for="pageNumber in pages.slice(page-1, page+5)" @click="page = pageNumber" :key="pageNumber"> {{pageNumber}} </button>
      </li>
      <li class="page-item">
        <button type="button" @click="page++" v-if="page < pages.length" class="page-link"> Next </button>
      </li>
    </ul>
  </nav>
  </div>
</template>

<script>
import Repository from "../repositories/RepositoryFactory"
const ActorRepository = Repository.get("actors")

export default {
  name: "ActorsHome",
  // components:{
  // },
  data(){
    return {
      actors: [],
      page: 1,
			perPage: 10,
			pages: [],
    }
  },
  methods: {
    async getActors() {
      const resp = await ActorRepository.get()
      console.log(resp)
      const data = resp['data']
      const new_data = []
      for (let obj of data){
        new_data.push({'actor_id':obj['actor_id'],
        'full_name': obj['first_name'].concat(' ',obj['last_name']),
        'last_update': obj['last_update']})
      }
      this.actors.push(...new_data)
    },
		setPages () {
      console.log('call set pages')
			let numberOfPages = Math.ceil(this.actors.length / this.perPage);
      console.log(numberOfPages)
			for (let index = 1; index <= numberOfPages; index++) {
				this.pages.push(index);
			}
		},
		paginate (actors) {
			let page = this.page;
			let perPage = this.perPage;
			let from = (page * perPage) - perPage;
			let to = (page * perPage);
			return  actors.slice(from, to);
		}
  },
  computed: {
    displayedPosts () {
      // this.setPages();
			return this.paginate(this.actors);
		}
  },
  watch:{
    actors:{
      deep: true,
      handler(){
        this.setPages();
      }

    }
  },
  created(){
    this.getActors();
  },
  filters: {
		trimWords(value){
			return value.split(" ").splice(0,20).join(" ") + '...';
		}
	}
}
</script>

<style scoped>
table, td, th{
  text-align:center
}

.link-style:hover{
  /*font-weight: bold;*/
  color: red;
  /*text-decoration: aqua;*/
}
button.page-link {
	display: inline-block;
}
button.page-link {
    font-size: 20px;
    color: blue;
    font-weight: 500;
}
.offset{
  width: 1000px !important;
  margin: 20px auto;
}
</style>