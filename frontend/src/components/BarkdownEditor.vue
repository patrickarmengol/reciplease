<script>
import { marked } from 'marked';

export default {
    props: ['message'],
    data() {
        // Bind the value of the message prop to a local data property
        return {
            editedMessage: this.message
        }
    },
    watch: {
        message(newValue) {
            this.editedMessage = newValue;
        }
    },
    computed: {
        compiledMarkdown() {
            return marked(this.editedMessage, { sanitize: true });
        }
    }
}
</script>

<template>
    <div class="editor">
        <textarea class="mdinput" v-model="editedMessage"></textarea>
        <div class="mdoutput" v-html="compiledMarkdown"></div>
    </div>
</template>

<style>
.editor {
    margin: 8vh 8vw;
    padding: 0;
    height: 74vh;
    background-color: #eeeeee;
    border: solid 2px #efefef;
    /* white-space: nowrap; */
    display: flex;
}


.mdinput,
.mdoutput {
    overflow: auto;
    width: 50%;
    height: 100%;
    box-sizing: border-box;
    padding: 0 20px;
}


.mdinput {
    border: none;
    border-right: 1px solid #ccc;
    resize: none;
    outline: none;
    background-color: #f6f6f6;
    font-size: 16px;
    font-family: 'Fira Code', monospace;
    padding: 20px;
}

.mdoutput img {
    width: 30%;
}
</style>
