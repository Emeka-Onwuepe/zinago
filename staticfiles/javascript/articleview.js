    Pagination();

    function Pagination() {
        var mainHeading = document.getElementById("mainHeading");
        var mainHeadingText = mainHeading.innerHTML;

        var sideNavUL = document.getElementById("sideNavUL");
        var li = sideNavUL.getElementsByTagName("li");

        for (i = 0; i < li.length; i++) {
            var mainHeadingmatch = li[i].getElementsByClassName("a")[0];
            var mainHeadingMatch = mainHeadingmatch.innerHTML;

            if (mainHeadingText === mainHeadingMatch) {
                li[i].style.backgroundColor = "#0FA6A6";
                mainHeadingmatch.style.color = "white";
            } else {
                li[i].style.backgroundColor = "";
            }

        }
    }

    Pagination2();

    function Pagination2() {
        var mainHeading = document.getElementById("mainHeading");
        var mainHeadingText = mainHeading.innerHTML;

        var sideNavUL = document.getElementById("sideNavUL2");
        var li = sideNavUL.getElementsByTagName("li");

        for (i = 0; i < li.length; i++) {
            var mainHeadingmatch = li[i].getElementsByClassName("a")[0];
            var mainHeadingMatch = mainHeadingmatch.innerHTML;

            if (mainHeadingText === mainHeadingMatch) {
                li[i].style.backgroundColor = "#0FA6A6";
                mainHeadingmatch.style.color = "white";
            } else {
                li[i].style.backgroundColor = "";
            }

        }
    }

    copyRightDate(2020)

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

    function SearchFunction() {
        var input, filter, sideNavUL, li, contents, i;
        input = document.getElementById("SearchInput");
        filter = input.value.toUpperCase();
        sideNavUL = document.getElementById("sideNavUL");
        li = sideNavUL.getElementsByTagName("li");
        for (i = 0; i < li.length; i++) {
            contents = li[i].getElementsByTagName("a")[0];
            if (contents.innerHTML.toUpperCase().indexOf(filter) > -1) {
                li[i].style.display = "block";
            } else {
                li[i].style.display = "none";

            }
        }
    }

    function SearchFunction2() {
        var input, filter, sideNavUL, li, contents, i;
        input = document.getElementById("SearchInput2");
        filter = input.value.toUpperCase();
        sideNavUL = document.getElementById("sideNavUL2");
        li = sideNavUL.getElementsByTagName("li");
        for (i = 0; i < li.length; i++) {
            contents = li[i].getElementsByTagName("a")[0];
            if (contents.innerHTML.toUpperCase().indexOf(filter) > -1) {
                li[i].style.display = "block";
            } else {
                li[i].style.display = "none";

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

    document.getElementsByTagName("BODY")[0].onresize = function() {
        myResize()
    };

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

    document.getElementsByTagName("BODY")[0].onscroll = function() {
        backToTop()
    };


    function backToTop() {
        var y_axis_offset = window.pageYOffset ||
            document.documentElement.scrollTop ||
            document.body.scrollTop;
        x = "1500";
        var backToTopButton = document.getElementById("backToTop");
        if (y_axis_offset >= x) {
            backToTopButton.style.display = "block";
        } else {
            backToTopButton.style.display = "none";
        }
    }

    //for Safari and his brothers
    window.addEventListener('scroll', function() {
        backToTop()
    });
    window.addEventListener('resize', function() {
        myResizeSafari()
    });
    var SafariDetector = !/function/.test(window.HTMLElement)

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

    try {
        let input = document.querySelector("#id_cv")
        input.accept = "application/pdf"
        let selectbox = document.querySelector("#id_job")
        let id = window.location.pathname.split('/')[1]
        selectbox.value = id.toString()
        selectbox.style.display = "none"
            // for (const label of selectbox.label) {
            //     console.log(label)
            // }
    } catch (error) {
        console.log(error)
    }