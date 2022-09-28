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

checkSideNav();

function checkSideNav() {
    var sideNav = document.getElementById("dropdown");
    var closeButton = document.getElementById("close");
    var toggle = document.getElementById("toggle")
    var x_axis = window.innerWidth;

    if (x_axis <= 899) {
        sideNav.style.display = "none";
        closeButton.style.display = "block";
        toggle.style.display = "block"
    } else {
        if (x_axis >= 899) {
            closeButton.style.display = "none"
            sideNav.style.display = "none";
            toggle.style.display = "none"
        }
    }
}

function show() {
    var sideNav = document.getElementById("dropdown");
    if (sideNav.style.display === "none") {
        sideNav.style.display = "block";
        var closeButton = document.getElementById("close");
        closeButton.style.display = "block";
    } else {
        showNot();
    };

};

function showNot() {
    var sideNav = document.getElementById("dropdown");
    sideNav.style.display = "none";
    var closeButton = document.getElementById("close");
    closeButton.style.display = "none";

}

// const dropDownBtn = document.querySelector(".drop")
// const dropDown = document.querySelector(".dropdown")

// dropDownBtn.addEventListener('mouseover', () => dropDown.style.display = "block")
// dropDownBtn.addEventListener('mouseout', () => dropDown.style.display = "none")

try {

    const dropDownBtn2 = document.querySelector(".drop2")
    const dropDown2 = document.querySelector(".dropdown2")

    dropDownBtn2.addEventListener('mouseover', () => dropDown2.style.display = "block")
    dropDownBtn2.addEventListener('mouseout', () => dropDown2.style.display = "none")

} catch (error) {
    console.log(error)
}

const dropDownBtns = document.querySelectorAll(".drops")

for (const btn of dropDownBtns) {
    const id = `.dropdown_${btn.id.split('_')[0]}`
    const dropdown = document.querySelector(id)
    btn.addEventListener('mouseover', () => {
        dropdown.style.display = "block"
        btn.style.backgroundColor = "white"
        dropdown.style.backgroundColor = "#f5f5f5"
    })
    btn.addEventListener('mouseout', () => { dropdown.style.display = "none" })

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

function myResize() {
    var closeButton = document.getElementById("close");
    var sideNav = document.getElementById("dropdown");
    var x_axis = window.innerWidth;
    if (x_axis >= 899) {
        sideNav.removeAttribute("style");
        closeButton.style.display = "none";
        checkSideNav();
    }
    if (x_axis <= 899 && document.activeElement.id !== "SearchInput") {
        sideNav.removeAttribute("style");
        if (document.activeElement.id !== "SearchInput") {
            checkSideNav()
        }

    }
}

//for Safari and his brothers
checkSideNavSafari();

function checkSideNavSafari() {
    var sideNav = document.getElementById("dropdown");
    var x_axis = document.documentElement.clientWidth ||
        document.body.clientWidth;
    var closeButton = document.getElementById("close");
    var toggle = document.getElementById("toggle")
    if (x_axis <= 899 && SafariDetector) {
        sideNav.style.display = "none";
        closeButton.style.display = "block";
        toggle.style.display = "block"
    } else {
        if (x_axis >= 899 && SafariDetector) {
            closeButton.style.display = "none"
            sideNav.style.display = "block";
            toggle.style.display = "none"
        }
    }
}


function myResizeSafari() {
    var closeButton = document.getElementById("close");
    var sideNav = document.getElementById("dropdown");
    var x_axis = document.documentElement.clientWidth ||
        document.body.clientWidth;
    var desktopView = 899
    if (x_axis >= desktopView && SafariDetector) {
        sideNav.removeAttribute("style");
        closeButton.style.display = "none";
        sideNav.style.display = "none";

    }
    if (x_axis <= desktopView && SafariDetector) {
        sideNav.removeAttribute("style");
        sideNav.style.position = "fixed";
    }
    checkSideNavSafari()
}


document.getElementsByTagName("BODY")[0].onscroll = function() {
    backToTop()
};

window.addEventListener('scroll', function() {
    backToTop()
});

document.getElementsByTagName("BODY")[0].onresize = function() {
    myResize()
};

//for Safari and his brothers
window.addEventListener('scroll', function() {
    backToTop()
});
window.addEventListener('resize', function() {
    myResizeSafari()
});
var SafariDetector = !/function/.test(window.HTMLElement)


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