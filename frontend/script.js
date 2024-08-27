const stud_name = document.getElementById('name');
const locate_btn = document.getElementById('locate');
const camID = document.getElementById('CamId');
const camID_btn = document.getElementById('CamId_btn');
const location_div = document.getElementById('location');
const location_div_h1 = document.getElementById('location_h1');
const result_div = document.getElementById('result');


const URI = "https://student-tracking-3gbzd03i9-nasheeths-projects.vercel.app"

locate_btn.addEventListener('click', () => {
    fetch(URI + "/locate/" + stud_name.value)  
        .then((res) => res.json())
        .then((data) => {
        location_div_h1.innerHTML = data.location;
        location_div.classList.remove('hide');
        }).catch((err) => {
            console.log(err);
        });
    });

camID_btn.addEventListener('click', () => {
    fetch(URI + "/camera/" + camID.value)  
        .then((res) => res.json())
        .then((data) => {
            var res = "";
        data.forEach(student => {
            res += `<li><img src="./assets/student.png" alt="student" class="studImg">${student.name}</li>`;
        });
        result_div.innerHTML = res;
        result_div.classList.remove('hide');
        }).catch((err) => {
            console.log(err);
        });
    });
