<template>
  <div class="offset mt-5">
    <router-link to="film_create"
    class="btn btn-success mt-3">ADD FILM</router-link>
    <table class="table table-bordered">
    <thead>
      <tr>
        <th>ID</th>
        <th>TITLE</th>
        <th>DESCRIPTION</th>
      </tr>
    </thead>
    <tbody>
    <tr v-for="film in displayedPosts" :key="film.film_id">
      <td >{{film.film_id}}</td>
      <td style="align-content:flex-start;">{{film.title}}</td>
      <td style="align-content:flex-start; word-wrap:break-word">{{film.description}}</td>
      <td><router-link class="link-style" :to="{name:'film_detail',params:{film_id:film.film_id}}">DETAIL</router-link></td>
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
const FilmRepository = Repository.get("films")

export default {
  name: "filmsHome",
  // components:{
  // },
  data(){
    return {
      films: [],
      page: 1,
			perPage: 10,
			pages: [],
    }
  },
  methods: {
    async getfilms() {
      const resp = await FilmRepository.get()
      console.log(resp)
      const data = resp['data']
      const new_data = []
      for (let obj of data){
        new_data.push({
          'film_id':obj['film_id'],
          'title': obj['title'],
          'description': obj['description']
          // 'release': obj['release_year'],
        })
      }
      this.films.push(...new_data)
    },
		setPages () {
      console.log('call set pages')
			let numberOfPages = Math.ceil(this.films.length / this.perPage);
      console.log(numberOfPages)
			for (let index = 1; index <= numberOfPages; index++) {
				this.pages.push(index);
			}
		},
		paginate (films) {
			let page = this.page;
			let perPage = this.perPage;
			let from = (page * perPage) - perPage;
			let to = (page * perPage);
			return  films.slice(from, to);
		}
  },
  computed: {
    displayedPosts () {
      // this.setPages();
			return this.paginate(this.films);
		}
  },
  watch:{
    films:{
      deep: true,
      handler(){
        this.setPages();
      }

    }
  },
  created(){
    this.getfilms();
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