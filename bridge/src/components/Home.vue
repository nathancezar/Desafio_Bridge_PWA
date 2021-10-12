<template>
  <div>
    <b-navbar 
      class=" header navbar navbar-light bg-light navbar-rounded shadow-sm"
      toggleable="lg">

      <b-navbar-brand
        href="/home">
      <b>Desafio bridge<span style="color: blue">_</span></b>
      </b-navbar-brand>
      
      <b-navbar-nav id="menuText" class="ml-auto">
        <b-nav-text><b>Desenvolvimento Web Full Stack</b></b-nav-text>
      </b-navbar-nav>

    </b-navbar>
    
    <div class="container">
      
      <template v-if="!loaded">
        <div class="d-flex justify-content-center my-5">
          <b-spinner label="Loading..."></b-spinner>
        </div>
      </template>
      
      <div v-show="loaded">
        <div class="container vertical-center mt-5">
          <div class="card w-50 mx-auto">
            <div class="card-body m-2">
              
              <div class="form-group text-left">
                <label for="number">Número</label>  
                <b-form-input
                  type="text"
                  class="form-control"
                  id="inputNumber"
                  v-model="inputNumber"
                  @keypress="validateNumber"
                  required>
                </b-form-input>
                <b-form-text id="number-help-block">
                  Insira um número real maior que 100.
                </b-form-text>
              </div>

              <b-button
                variant="primary"
                block
                type="submit"
                :disabled="inputNumber < 100"
                @click="sendNumber">
              Calcular menor duodigito
              </b-button>

              <div v-if="result" class="form-group text-left mt-3">
                <b-form-textarea 
                  id=resultText
                  v-model="result"
                  no-resize
                  readonly
                  :value="result">

                </b-form-textarea>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { BNavbar } from 'bootstrap-vue'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    BNavbar
  },
  data() {
    return {
      inputNumber: '',
      loaded: true,
      getResult: false,
      result: '',
    }
  },
  methods: {
    validateNumber: event => {
      const charCode = String.fromCharCode(event.keyCode);
      if (!/[0-9]/.test(charCode)) {
        event.preventDefault();
      }
    },
    sendNumber() {
      this.loaded = false;
      console.log(this.inputNumber);
      axios.post(this.backend + '/calculate', {
        'number': this.inputNumber,
      }).then((res) => {
        if(res.data) {
          console.log(res.data);
          this.result = this.result +
                        res.data.duodigit +
                        ' Tempo de execução: ' +
                        res.data.time +
                        '\n';
        }
        this.loaded = true;
      }).catch(err => console.log(err));
      this.loaded = true; // retirar depois de implementar o backend
    }
  }
}
</script>

<style>

</style>