<template>
    <form id="app" @submit.prevent="getLogin">
        <div class="container">
            <center>
                <h1>REGISTRATION</h1>
            </center>
            <hr>
            <br>
            <div>
                <label for="name"><b>Name</b></label>
                <label class="star">*</label>
                <br>
                <br>
                <input type="text" placeholder="Enter your name" v-model="name" />
                <span v-if="!$v.name.required && $v.name.$dirty" class="text-danger">Name is required!</span>
                <span v-if="!$v.name.alpha && $v.name.$dirty" class="text-danger">Name is Alphabetic!</span>
            </div>

            <br>
            <div>
                <label for="mail"><b>Email</b></label>
                <label class="star">*</label>
                <br>
                <br>
                <input type="email" placeholder="ram@gmail.com" v-model="email">
                <br>
                <span v-if="!$v.name.required && $v.name.$dirty" class="text-danger">Emailis required!</span>
            </div>

            <br>
            <div>
                <label for="phone"><b>Phone Number</b></label>
                <label class="star">*</label>
                <br><br>
                <input type="text" placeholder="Enter your phone number" v-model="phone" />
                <span v-if="!$v.name.required && $v.name.$dirty" class="text-danger">Name is required!</span>
                <span v-if="!$v.name.alpha && $v.name.$dirty" class="text-danger">Name is Alphabetic!</span>
            </div>
            <br>
            <br>
            <div>
                <label for="gender"><b>Gender</b></label>
                <label class="star">*</label>
                <br><br>
                <input type="radio" values="male" id="male" name="gender" v-model="gender" />
                &nbsp;
                <label for="male">Male</label>
                &nbsp;&nbsp;
                <input type="radio" values="female" id="female" name="gender" v-model="gender" />
                &nbsp;
                <label for="female">Female</label>
                &nbsp;&nbsp;
                <input type="radio" values="others" id="others" name="gender" v-model="gender" />
                &nbsp;
                <label for="others">Others</label>

                <br>
                <span v-if="!$v.gender.required && $v.name.$dirty" class="text-danger">Required field</span>
                <br>
                <br>
            </div>
            <div>
                <label for="password"><b>Password</b></label>
                <label class="star">*</label>
                <br><br>
                <input type="password" placeholder="Enter your password" v-model="password" />
                <br>
                <span v-if="!$v.password.required && $v.name.$dirty" class="text-danger">Password required
                    required!</span>
                <span v-if="!$v.password.minLength && $v.name.$dirty" class="text-danger">Mininmun 6 character
                    required!</span>
                <span v-if="!$v.password.maxLentgth && $v.name.$dirty" class="text-danger">Maximum 18 character
                    required!!</span>
                <br>
                <br>
            </div>
            <div>
                <label for="confirm password"><b>Confirm Password</b></label>
                <label class="star">*</label>
                <br><br>
                <input type="password" placeholder="confirm password" v-model="confirm_password" />
                <br>
                <span v-if="!$v.confirm_password.required && $v.name.$dirty" class="text-danger">Password required
                    required!</span>
                <span v-if="!$v.confirm_password.minLength && $v.name.$dirty" class="text-danger">Mininmun 6 character
                    required!</span>
                <span v-if="!$v.confirm_password.maxLentgth && $v.name.$dirty" class="text-danger">Maximum 18 character
                    required!!</span>
                <span v-if="!$v.confirm_password.sameAs && $v.name.$dirty" class="text-danger">Must be same as
                    password</span>
                <br>
                <br>
            </div>
            <div>
                <label for="name"><b>Terms and Conditions</b></label>
                <br><br>
                <input type="checkbox" values="terms" id="terms" />
                &nbsp;
                <label for="terms">Accept</label>
                <br>
                <span v-if="!$v.check.required && $v.name.$dirty" class="text-danger">Required field</span>
                <br>
                <br>
            </div>
            <div>
                <button type="submit" @click="getLogin" class="registerbtn">LOGIN</button>
            </div>
        </div>
    </form>

</template>

<script>
import {
    required,
    alpha,
    email,
    minLength,
    maxLength,
    sameAs,
    numeric
} from "vuelidate/lib/validators";

export default {
    name: "LoGin",

    data: () => ({
        name: "",
        email: '',
        phone: '',
        gender: ['male', 'emale'],
        password: '',
        confirm_password: '',
        check: '',
    }),
    validations: {
        name: {
            required,
            alpha,
            minLength: minLength(3),
            maxLength: maxLength(25)
        },
        email:
        {
            required,
            email,
        },
        password:
        {
            required,
            minLength: minLength(6),
            maxLength: maxLength(18)
        },
        gender: ['male', 'emale'],
        confirm_password:
        {
            required,
            minLength: minLength(6),
            maxLength: maxLength(18),
            sameAsPassword: sameAs("password")
        },
        check:
        {
            required,
        },
        phone:
        {   required,
            numeric,
            minLength: minLength(10),
            maxLength: maxLength(10),
        }
    },
    methods: {
        getLogin() {
            this.$v.$touch();

            if (!this.$v.$invalid) {

                console.log(`Name: ${this.name}`)
            }
        }
    }
}
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: #211f2f;
}

/* Add padding to containers */
.container {
    padding: 16px;
    background-color: white;
    font-size: 18px;
    border-radius: 10px;
    border: 1px solid rgba(10, 2, 2, 0.5);
    box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.5);
}

.container {

    width: 550px;
    margin: 3px auto 0px auto;
    text-align: initial;
    padding: 60px;
}


* {
    box-sizing: border-box;
}

/* Full-width input fields */
input[type=text],
input[type=password],
input[type=email] {
    width: 400px;
    border: 1px solid #ddd;
    border-radius: 3px;
    outline: 0;
    padding: 10px;
    background-color: #fff;
}

input[type=text]:focus,
input[type=password]:focus {
    background-color: #ddd;
    outline: none;
}

.star {
    color: red;
}

/* Set a style for the submit button */

.registerbtn {
    align-items: center;
    text-align: center;
    padding: 7px;
    font-size: 16px;
    font-family: sans-serif;
    font-weight: 600;
    border: none;
    border-radius: 3px;
    background-color: rgba(7, 7, 7, 0.8);
    color: #fff;
    cursor: pointer;
    border: 1px solid rgba(245, 242, 242, 0.3);
    box-shadow: 1px 1px 5px rgba(236, 227, 227, 0.3);
    margin-bottom: 20px;

}

.registerbtn {
    height: 60px;
    width: 400px;
    background-color: #211f2f;
    color: white;
    font-size: 20px;
}

.registerbtn:hover {
    opacity: 1;
}

.text-danger {
    font-size: 12px;
    color: red;
}
</style>