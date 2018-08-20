<template>
  <section>
    <div>
      <a href=""><img src="url"></a>
      <div>{{text}}</div>
      <div>
        <span>{{price}}</span>
        <span>{{amount}}</span>
      </div>
    </div>
    <div>

    </div>
  </section>
</template>

<script>
export default {
  name: 'courseblock',
  data() {
    return {

    }
  },
  props: {
    url: String,
    text: String,
    price: String,
    amount: Number
  }
}
</script>
