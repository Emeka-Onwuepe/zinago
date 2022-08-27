copyRightDate(2022)

function copyRightDate(x) {
    var d = new Date;
    var year = d.getFullYear();
    var footerDate = document.getElementById("footerdate");
    if (year == x) {
        footerDate.innerHTML = year;
    } else {
        footerDate.innerHTML = x + "-" +
            year;
    }
}

const dropDownBtn = document.querySelector(".drop")
const dropDown = document.querySelector(".dropdown")

dropDownBtn.addEventListener('mouseover', () => dropDown.style.display = "block")
dropDownBtn.addEventListener('mouseout', () => dropDown.style.display = "none")

var i = 0;
var ind = 0;

var slidePanel = document.getElementById("slidetext");
slidetext();

function slidetext() {
    var text1 = "We offer solutions we have gained through experience, employment, law and best practices ";
    var text2 = "We offer flexible, customized services, as we believe there is no one-size fits all model";

    if (i < text1.length) {
        slidePanel.innerHTML += text1.charAt(i)


    }

    if (i == text1.length) {
        slidePanel.innerHTML = "";
    }
    if (i > text1.length) {
        slidePanel.innerHTML += text2.charAt(ind)
        ind++;
        if (i == text2.length + 1 + text1.length) {
            ind = 0;
        }
    }
    if (i == text2.length + 1 + text1.length) {
        slidePanel.innerHTML = "";
        i = -1;
    }
    i++;
    setTimeout(slidetext, 170);
}

const backToTop = () => {
    let y_axis_offset = window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
    x = "300";
    let backToTopButton = document.getElementById("backToTop");
    if (y_axis_offset >= x) {
        backToTopButton.style.display = "block";
    } else {
        backToTopButton.style.display = "none";
    }
}

document.getElementsByTagName("BODY")[0].onscroll = function() {
    backToTop()
};

window.addEventListener('scroll', function() {
    backToTop()
});