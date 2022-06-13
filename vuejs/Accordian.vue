<template>
  <div class="boder-2 p-2 rounded">
    <div class="main">
       <button class="accordion" @click='toggle()'>{{title}}</button>
    </div>
    <div class="panel"  v-show="isOpen">
      <slot>
          <p>Lorem ipsum...</p>

      </slot>
    </div>
    



  </div>
</template>


<script>
export default
  {
    name: 'Accor_Dians',
    props:
    {
      title:String
    },

  
      data: ()=> {
        return{
          isOpen:false
        }
      
    },
   methods:{
        toggle: function(){
            this.isOpen = !this.isOpen
        }
    }
  };
</script>
<style>
.main {
  
  color: white;
  padding: 5px;
  border-radius: 5px;
  font-style: italic;
}

.border {
  border: 2;
  padding: 2;
}

.accordion {
  background-color: #eee;
  color: #444;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  transition: 0.4s;
}

.accordion:after {
  content: '\002B';
  color: #777;
  font-weight: bold;
  float: right;
  margin-left: 5px;
}


</style>