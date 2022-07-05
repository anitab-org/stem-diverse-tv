(window.webpackJsonp=window.webpackJsonp||[]).push([[28],{112:function(e,t,n){"use strict";n.d(t,"a",(function(){return b})),n.d(t,"b",(function(){return m}));var r=n(0),a=n.n(r);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function s(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var u=a.a.createContext({}),l=function(e){var t=a.a.useContext(u),n=t;return e&&(n="function"==typeof e?e(t):s(s({},t),e)),n},b=function(e){var t=l(e.components);return a.a.createElement(u.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.a.createElement(a.a.Fragment,{},t)}},h=a.a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,i=e.parentName,u=c(e,["components","mdxType","originalType","parentName"]),b=l(n),h=r,m=b["".concat(i,".").concat(h)]||b[h]||p[h]||o;return n?a.a.createElement(m,s(s({ref:t},u),{},{components:n})):a.a.createElement(m,s({ref:t},u))}));function m(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,i=new Array(o);i[0]=h;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:r,i[1]=s;for(var u=2;u<o;u++)i[u]=n[u];return a.a.createElement.apply(null,i)}return a.a.createElement.apply(null,n)}h.displayName="MDXCreateElement"},98:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return i})),n.d(t,"metadata",(function(){return s})),n.d(t,"toc",(function(){return c})),n.d(t,"default",(function(){return l}));var r=n(3),a=n(7),o=(n(0),n(112)),i={title:"How to Contribute",slug:"/Contribution/how_to_contribute"},s={unversionedId:"how_to_contribute",id:"how_to_contribute",isDocsHomePage:!1,title:"How to Contribute",description:"First of all, thank you for the interest in contributing to the STEM Diverse TV!",source:"@site/docs/how_to_contribute.md",slug:"/Contribution/how_to_contribute",permalink:"/stem-diverse-tv/docs/Contribution/how_to_contribute",editUrl:"https://github.com/anitab-org/stem-diverse-tv/tree/master/docs/docs/how_to_contribute.md",version:"current",sidebar:"docs",previous:{title:"Reporting Guidelines",permalink:"/stem-diverse-tv/docs/Guidelines/reporting_guidelines"},next:{title:"Commit Message Style Guide",permalink:"/stem-diverse-tv/docs/Contribution/commit_message_structure"}},c=[{value:"Code",id:"code",children:[]},{value:"Quality Assurance",id:"quality-assurance",children:[]},{value:"Documentation",id:"documentation",children:[]},{value:"Outreach/Training/Research",id:"outreachtrainingresearch",children:[]},{value:"User Interface",id:"user-interface",children:[]}],u={toc:c};function l(e){var t=e.components,n=Object(a.a)(e,["components"]);return Object(o.b)("wrapper",Object(r.a)({},u,n,{components:t,mdxType:"MDXLayout"}),Object(o.b)("p",null,"First of all, thank you for the interest in contributing to the STEM Diverse TV!"),Object(o.b)("p",null,"Any issue labeled as ",Object(o.b)("a",{parentName:"p",href:"https://github.com/anitab-org/stem-diverse-tv/issues?q=is%3Aissue+is%3Aopen+label%3A%22Status%3A+Available%22"},"Status: Available")," or ",Object(o.b)("a",{parentName:"p",href:"https://github.com/anitab-org/stem-diverse-tv/issues?q=is%3Aissue+is%3Aopen+label%3A%22First+Timers+Only%22"},"First Timers Only")," can be worked by any contributor."),Object(o.b)("p",null,"Issues labeled as ",Object(o.b)("inlineCode",{parentName:"p"},"First Timers Only")," are more oriented towards newcomers, with the exception of Quality Assurance issues that can be worked by any contributor because there can always be some bug and these issues are always available."),Object(o.b)("p",null,"There are many ways you can contribute to this project."),Object(o.b)("ul",null,Object(o.b)("li",{parentName:"ul"},Object(o.b)("strong",{parentName:"li"},"Test the backend for Quality Assurance")," purposes and ",Object(o.b)("strong",{parentName:"li"},"report bugs")," (if any);"),Object(o.b)("li",{parentName:"ul"},Object(o.b)("strong",{parentName:"li"},"Give feedback")," on what is shared with the community (UI prototype, suggesting new features); "),Object(o.b)("li",{parentName:"ul"},Object(o.b)("strong",{parentName:"li"},"Participate in discussions")," on Slack; "),Object(o.b)("li",{parentName:"ul"},Object(o.b)("strong",{parentName:"li"},"Solving the available issues"),", implement features, fix bugs, develop tests, etc...;"),Object(o.b)("li",{parentName:"ul"},Object(o.b)("strong",{parentName:"li"},"Helping others")," understand the project ",Object(o.b)("strong",{parentName:"li"},"on Slack"),";"),Object(o.b)("li",{parentName:"ul"},"Review pull requests (PRs), even if you're a newcomer.")),Object(o.b)("h2",{id:"code"},"Code"),Object(o.b)("p",null,"You can help on the development. You can check the contribution guidelines for this, ",Object(o.b)("inlineCode",{parentName:"p"},"CONTRIBUTING.md")," file inside ",Object(o.b)("inlineCode",{parentName:"p"},".github")," folder."),Object(o.b)("p",null,"Before starting to contribute make sure to check our ",Object(o.b)("a",{parentName:"p",href:"https://github.com/anitab-org/stem-diverse-tv/wiki/Commit-Message-Style-Guide"},"Commit Message Style Guide"),"."),Object(o.b)("p",null,"You can check existing issues that are available and not assigned to anyone. You can filter also issues with labels such as ",Object(o.b)("a",{parentName:"p",href:"https://github.com/anitab-org/stem-diverse-tv/issues?q=is%3Aissue+is%3Aopen+label%3A%22Category%3A+Coding%22"},"Category: Coding")," which are available ",Object(o.b)("a",{parentName:"p",href:"https://github.com/anitab-org/stem-diverse-tv/issues?q=is%3Aissue+is%3Aopen+label%3A%22Status%3A+Available%22"},"Status: Available"),"."),Object(o.b)("p",null,"You can find a bugs while testing and submit an issue to solve them."),Object(o.b)("p",null,"You can find more about ",Object(o.b)("a",{parentName:"p",href:"https://github.com/anitab-org/stem-diverse-tv/wiki/Tech-Stack"},"Tech Stack here"),"."),Object(o.b)("h2",{id:"quality-assurance"},"Quality Assurance"),Object(o.b)("p",null,"You can test the backend for bugs. We have a set of ",Object(o.b)("a",{parentName:"p",href:"https://github.com/anitab-org/stem-diverse-tv/wiki/Quality-Assurance"},"Quality Assurance Test Cases")," to help you with test the backend to lookup these bugs."),Object(o.b)("p",null,Object(o.b)("strong",{parentName:"p"},"If you find any bug you can report")," by creating an issue, using the ",Object(o.b)("strong",{parentName:"p"},"Bug report template"),". Here's a nice ",Object(o.b)("a",{parentName:"p",href:"https://github.com/anitab-org/stem-diverse-tv/issues/7"},"example of a Bug Report issue"),".\nThese types of reports are very important because we can detect bugs in the backend and then create issues that fix these bugs. Also if you're not comfortable with the code you can just report a bugs you find, without having to suggest a solution on it, and thats a valuable contribution to the project."),Object(o.b)("p",null,Object(o.b)("strong",{parentName:"p"},"Tools")," you can use to do this: "),Object(o.b)("ul",null,Object(o.b)("li",{parentName:"ul"},Object(o.b)("strong",{parentName:"li"},"Swagger UI")," provided in root of the deployed server. You can check the deployed server link in the the README.md file of the project. You can learn more about ",Object(o.b)("a",{parentName:"li",href:"https://github.com/anitab-org/stem-diverse-tv/wiki/Using-Swagger-UI"},"how to use Swagger here"),"."),Object(o.b)("li",{parentName:"ul"},Object(o.b)("a",{parentName:"li",href:"https://www.getpostman.com/"},"Postman")," to make your HTTP requests to the backend without being limited by Swagger API. E.g.: With this you can see the results of not sending an authorization token, which with the Swagger UI you're not allowed to do it.")),Object(o.b)("h2",{id:"documentation"},"Documentation"),Object(o.b)("p",null,"TBD"),Object(o.b)("h2",{id:"outreachtrainingresearch"},"Outreach/Training/Research"),Object(o.b)("p",null,"For this you can promote the project in whatever way you feel comfortable with.\nHere's some examples:"),Object(o.b)("ul",null,Object(o.b)("li",{parentName:"ul"},"You can write blog posts about the project, something you learned from it, or you want to share with others;"),Object(o.b)("li",{parentName:"ul"},"Research about ways to improve the project and discuss it with the Community on the Slack;"),Object(o.b)("li",{parentName:"ul"},"Participate on the project's discussion on the ",Object(o.b)("a",{parentName:"li",href:"https://anitab-org.zulipchat.com/#narrow/stream/225705-STEM-diverse-tv"},"#STEM-diverse-tv")," zulip channel;"),Object(o.b)("li",{parentName:"ul"},"Help other contributors or newcomers learn and understand the project;"),Object(o.b)("li",{parentName:"ul"},"etc ...")),Object(o.b)("h2",{id:"user-interface"},"User Interface"),Object(o.b)("p",null,"User interface is created using Applicaster Platform and we plan to support following platforms:"),Object(o.b)("ul",null,Object(o.b)("li",{parentName:"ul"},"Android mobile"),Object(o.b)("li",{parentName:"ul"},"Android TV"),Object(o.b)("li",{parentName:"ul"},"Amazon Fire TV"),Object(o.b)("li",{parentName:"ul"},"iOS mobile"),Object(o.b)("li",{parentName:"ul"},"TvOS (Apple TV)"),Object(o.b)("li",{parentName:"ul"},"Samsung Smart TV"),Object(o.b)("li",{parentName:"ul"},"LG Smart TV"),Object(o.b)("li",{parentName:"ul"},"Roku TV")),Object(o.b)("h1",{id:"one-last-thing"},"One last thing..."),Object(o.b)("p",null,"If you have any doubts about the project or how to contribute do not hesitate to ask questions on GitHub or on ",Object(o.b)("a",{parentName:"p",href:"https://anitab-org.zulipchat.com/"},"Zulip"),". The community will do their best to help you out :)"))}l.isMDXComponent=!0}}]);