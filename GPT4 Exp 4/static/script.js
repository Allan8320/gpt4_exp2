/* ============================================================
   CONTENT AI - JAVASCRIPT
   ============================================================ */


let currentBlog = "";

let currentExtra = "";

let toastTimer;


/* ============================================================
   NAVIGATION
   ============================================================ */

function showSection(section, clickedButton) {

    const studio =
        document.getElementById("studioSection");

    const seo =
        document.getElementById("seoSection");

    const assistant =
        document.getElementById("assistantSection");


    studio.classList.add("hidden-section");

    seo.classList.add("hidden-section");

    assistant.classList.add("hidden-section");


    if (section === "studio") {

        studio.classList.remove("hidden-section");

    }


    if (section === "seo") {

        seo.classList.remove("hidden-section");

    }


    if (section === "assistant") {

        assistant.classList.remove("hidden-section");

    }


    document
        .querySelectorAll(".nav-item")
        .forEach(function(button) {

            button.classList.remove("active");

        });


    if (clickedButton) {

        clickedButton.classList.add("active");

    }


    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}


/* ============================================================
   API HELPER
   ============================================================ */

async function apiRequest(url, data) {

    try {

        const response = await fetch(
            url,
            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)

            }
        );


        const result = await response.json();


        if (!response.ok) {

            throw new Error(
                result.error || "Something went wrong."
            );

        }


        return result;

    }

    catch (error) {

        showToast(
            error.message,
            "!"
        );

        throw error;

    }

}


/* ============================================================
   GENERATE BLOG
   ============================================================ */

async function generateBlog() {

    const topic =
        document.getElementById("topic").value.trim();

    const style =
        document.getElementById("style").value;

    const tone =
        document.getElementById("tone").value;

    const wordCount =
        document.getElementById("word_count").value;


    if (!topic) {

        showToast(
            "Please enter a blog topic.",
            "!"
        );

        document
            .getElementById("topic")
            .focus();

        return;

    }


    const button =
        document.getElementById("generateButton");

    const loading =
        document.getElementById("loading");

    const empty =
        document.getElementById("emptyBlog");

    const output =
        document.getElementById("blogOutput");


    button.disabled = true;

    button.innerHTML =
        "Generating...";


    loading.style.display = "flex";

    empty.style.display = "none";

    output.classList.remove("visible");


    try {

        const data = await apiRequest(
            "/generate-blog",
            {

                topic: topic,

                style: style,

                tone: tone,

                word_count: wordCount

            }
        );


        currentBlog = data.blog;


        output.textContent =
            currentBlog;


        output.classList.add("visible");


        showToast(
            "Blog generated successfully.",
            "✓"
        );


    }

    catch (error) {

        empty.style.display = "flex";

    }


    loading.style.display = "none";

    button.disabled = false;

    button.innerHTML =
        "<span>✦</span> Generate Blog";

}


/* ============================================================
   CHECK BLOG
   ============================================================ */

function requireBlog() {

    if (!currentBlog) {

        showToast(
            "Generate a blog first.",
            "!"
        );

        return false;

    }

    return true;

}


/* ============================================================
   SHOW EXTRA RESULT
   ============================================================ */

function showExtra(title, content) {

    currentExtra = content;


    const card =
        document.getElementById("extraCard");

    const titleElement =
        document.getElementById("extraTitle");

    const output =
        document.getElementById("extraOutput");


    titleElement.textContent =
        title;

    output.textContent =
        content;


    card.classList.remove("hidden");


    card.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });

}


/* ============================================================
   TITLES
   ============================================================ */

async function generateTitles() {

    if (!requireBlog()) {
        return;
    }


    showToast(
        "Generating titles...",
        "✦"
    );


    try {

        const data = await apiRequest(
            "/generate-titles",
            {
                blog: currentBlog
            }
        );


        showExtra(
            "Suggested Blog Titles",
            data.titles
        );


        showToast(
            "Titles generated.",
            "✓"
        );

    }

    catch (error) {

        console.log(error);

    }

}


/* ============================================================
   KEYWORDS
   ============================================================ */

async function generateKeywords() {

    if (!requireBlog()) {
        return;
    }


    showToast(
        "Generating SEO keywords...",
        "✦"
    );


    try {

        const data = await apiRequest(
            "/generate-keywords",
            {
                blog: currentBlog
            }
        );


        showExtra(
            "SEO Keywords",
            data.keywords
        );


        showToast(
            "Keywords generated.",
            "✓"
        );

    }

    catch (error) {

        console.log(error);

    }

}


/* ============================================================
   SUMMARY
   ============================================================ */

async function generateSummary() {

    if (!requireBlog()) {
        return;
    }


    showToast(
        "Creating summary...",
        "✦"
    );


    try {

        const data = await apiRequest(
            "/generate-summary",
            {
                blog: currentBlog
            }
        );


        showExtra(
            "100-Word Summary",
            data.summary
        );


        showToast(
            "Summary generated.",
            "✓"
        );

    }

    catch (error) {

        console.log(error);

    }

}


/* ============================================================
   META DESCRIPTION
   ============================================================ */

async function generateMeta() {

    if (!requireBlog()) {
        return;
    }


    showToast(
        "Creating meta description...",
        "✦"
    );


    try {

        const data = await apiRequest(
            "/generate-meta",
            {
                blog: currentBlog
            }
        );


        showExtra(
            "SEO Meta Description",
            data.meta
        );


        showToast(
            "Meta description generated.",
            "✓"
        );

    }

    catch (error) {

        console.log(error);

    }

}


/* ============================================================
   SEO PAGE RESULT
   ============================================================ */

function showSEOResult(title, content) {

    currentExtra = content;


    const card =
        document.getElementById("seoResultCard");

    const titleElement =
        document.getElementById("seoResultTitle");

    const output =
        document.getElementById("seoResultOutput");


    titleElement.textContent =
        title;

    output.textContent =
        content;


    card.classList.remove("hidden");


    card.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });

}


/* ============================================================
   COPY BLOG
   ============================================================ */

async function copyBlog() {

    if (!currentBlog) {

        showToast(
            "There is no blog to copy.",
            "!"
        );

        return;

    }


    try {

        await navigator.clipboard.writeText(
            currentBlog
        );


        showToast(
            "Blog copied to clipboard.",
            "✓"
        );

    }

    catch {

        showToast(
            "Unable to copy.",
            "!"
        );

    }

}


/* ============================================================
   COPY EXTRA
   ============================================================ */

async function copyExtra() {

    if (!currentExtra) {

        showToast(
            "Nothing to copy.",
            "!"
        );

        return;

    }


    try {

        await navigator.clipboard.writeText(
            currentExtra
        );


        showToast(
            "Content copied.",
            "✓"
        );

    }

    catch {

        showToast(
            "Unable to copy.",
            "!"
        );

    }

}


/* ============================================================
   DOWNLOAD BLOG
   ============================================================ */

function downloadBlog() {

    if (!currentBlog) {

        showToast(
            "Generate a blog first.",
            "!"
        );

        return;

    }


    const blob =
        new Blob(
            [currentBlog],
            {
                type: "text/plain"
            }
        );


    const url =
        URL.createObjectURL(blob);


    const link =
        document.createElement("a");


    link.href = url;

    link.download =
        "generated_blog.txt";


    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);


    URL.revokeObjectURL(url);


    showToast(
        "Blog downloaded.",
        "✓"
    );

}


/* ============================================================
   CHATBOT
   ============================================================ */

async function sendMessage() {

    const input =
        document.getElementById("chatInput");

    const message =
        input.value.trim();


    if (!message) {

        return;

    }


    addChatMessage(
        message,
        "user"
    );


    input.value = "";


    const loadingId =
        addChatMessage(
            "Thinking...",
            "ai",
            true
        );


    try {

        const data = await apiRequest(
            "/chat",
            {

                message: message,

                blog: currentBlog

            }
        );


        removeChatMessage(
            loadingId
        );


        addChatMessage(
            data.response,
            "ai"
        );


        /*
         * If chatbot generated a new blog,
         * update the main blog area as well.
         */

        if (data.blog) {

            currentBlog =
                data.blog;


            const output =
                document.getElementById(
                    "blogOutput"
                );


            const empty =
                document.getElementById(
                    "emptyBlog"
                );


            output.textContent =
                currentBlog;


            output.classList.add(
                "visible"
            );


            empty.style.display =
                "none";

        }


    }

    catch (error) {

        removeChatMessage(
            loadingId
        );

    }

}


/* ============================================================
   ADD CHAT MESSAGE
   ============================================================ */

function addChatMessage(
    message,
    type,
    temporary = false
) {

    const chat =
        document.getElementById(
            "chatMessages"
        );


    const wrapper =
        document.createElement("div");


    wrapper.className =
        "chat-message " + type;


    if (temporary) {

        wrapper.dataset.temporary =
            "true";

    }


    const avatar =
        document.createElement("div");


    avatar.className =
        "message-avatar";


    avatar.textContent =
        type === "ai"
            ? "✦"
            : "A";


    const content =
        document.createElement("div");


    content.className =
        "message-content";


    const name =
        document.createElement("strong");


    name.textContent =
        type === "ai"
            ? "ContentAI"
            : "You";


    const paragraph =
        document.createElement("p");


    paragraph.textContent =
        message;


    content.appendChild(name);

    content.appendChild(paragraph);


    wrapper.appendChild(avatar);

    wrapper.appendChild(content);


    chat.appendChild(wrapper);


    chat.scrollTop =
        chat.scrollHeight;


    return wrapper;

}


/* ============================================================
   REMOVE CHAT MESSAGE
   ============================================================ */

function removeChatMessage(element) {

    if (element && element.parentNode) {

        element.parentNode.removeChild(
            element
        );

    }

}


/* ============================================================
   CHAT ENTER KEY
   ============================================================ */

function handleChatKey(event) {

    if (event.key === "Enter") {

        event.preventDefault();

        sendMessage();

    }

}


/* ============================================================
   CHAT SUGGESTIONS
   ============================================================ */

function useSuggestion(message) {

    const input =
        document.getElementById(
            "chatInput"
        );


    input.value =
        message;


    input.focus();

}


/* ============================================================
   TOAST
   ============================================================ */

function showToast(
    message,
    icon = "✓"
) {

    const toast =
        document.getElementById(
            "toast"
        );

    const toastMessage =
        document.getElementById(
            "toastMessage"
        );

    const toastIcon =
        document.getElementById(
            "toastIcon"
        );


    toastMessage.textContent =
        message;

    toastIcon.textContent =
        icon;


    toast.classList.add(
        "show"
    );


    clearTimeout(
        toastTimer
    );


    toastTimer =
        setTimeout(
            function() {

                toast.classList.remove(
                    "show"
                );

            },
            3000
        );

}


/* ============================================================
   ABOUT MODAL
   ============================================================ */

function showAbout() {

    document
        .getElementById("aboutModal")
        .classList.add("show");

}


function hideAbout() {

    document
        .getElementById("aboutModal")
        .classList.remove("show");

}


function closeAbout(event) {

    if (
        event.target.id ===
        "aboutModal"
    ) {

        hideAbout();

    }

}


/* ============================================================
   INITIALIZATION
   ============================================================ */

document.addEventListener(
    "DOMContentLoaded",
    function() {

        /*
         * Make sure the studio is selected
         * when the application starts.
         */

        showSection(
            "studio",
            document.querySelector(
                ".nav-item.active"
            )
        );

    }
);