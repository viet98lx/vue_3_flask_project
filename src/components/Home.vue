<template>
<!--<h1>this is home page</h1>-->
<div class="container mt-5">
<!--  <router-link class="link-style" :to="/">This is home page</router-link>-->
  <h2 class="remove-whitespace">HOT MEME</h2>
  <div v-if="images.length">
    <div class="gallery">
      <div class="gallery-panel"
           v-for="photo in images"
           :key="photo.name">
          <img :src='photo.sample'>
      </div>
    </div>
  </div>

<!--  <div v-if="images">-->
<!--    <img v-bind:src="images[0].sample" />-->
<!--  </div>-->
</div>

</template>

<script>
// import {Carousel, Slide} from 'vue-carousel'
export default {
  name: "Home",
  components:{
    // Carousel,
    // Slide
  },
  data(){
    return {
      actors: [],
      images:[
          {
            name: 'meme_1',
          sample: require('@/assets/meme_1.jpg')
        },
          {
            name: 'meme_6',
          sample: require('@/assets/meme_10.jpg')
        },
          {
            name: 'meme_2',
          sample: require('@/assets/meme_2.png')
        },
          {
            name: 'meme_3',
          sample: require('@/assets/meme_3.png')
        },
          {
            name: 'meme_4',
          sample: require('@/assets/meme_4.png')
        },
          {
            name: 'meme_5',
          sample: require('@/assets/meme_5.png')
        },
          {
            name: 'meme_6',
          sample: require('@/assets/meme_6.png')
        },
          {
            name: 'meme_7',
          sample: require('@/assets/meme_7.jpg')
        },
          {
            name: 'meme_8',
          sample: require('@/assets/meme_8.jpg')
        },
          {
            name: 'meme_9',
          sample: require('@/assets/meme_9.jpg')
        },
          {
            name: 'meme_11',
          sample: require('@/assets/meme_11.jpg')
        },
          {
            name: 'meme_12',
          sample: require('@/assets/meme_12.jpg')
        }
      ]
    }
  },
  methods: {
  },
  created(){
    // this.getActors()
    // this.images.sample = '../assets/logo.png'
  }
}
</script>

<style scoped>
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
    grid-gap: 1rem;
    max-width: 80rem;
    margin: 5rem auto;
    padding: 0 5rem;
  }
.gallery-panel img {
  width: 100%;
  height: 22vw;
  object-fit: cover;
  border-radius: 0.75rem;
}
h2.remove-whitespace{
  color:brown;
  text-align:center;
  margin: 0;
  padding: 0;
}
</style>