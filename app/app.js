// Request html canvas element
var canvas = document.getElementById("canvas");

// Create a WebGL rendering context  
var gl = canvas.getContext("webgl2");

// Tell user if their browser does not support WebGL
if (!gl) {
    alert("Your browser does not support WebGL");
}

// Set the color of the canvas.
// Parameters are RGB colors (red, green, blue, alpha)
gl.clearColor(0, 0.6, 0.0, 1.0);
// Clear the color buffer with specified color
gl.clear(gl.COLOR_BUFFER_BIT);

const shaders = {
    vs: `#version 300 es
        in vec2 vertPosition;
        in vec3 vertColor;
        out vec3 fragColor;
     
        void main() {
            fragColor = vertColor;
            gl_Position = vec4(vertPosition, 0, 1);
        }`,
 
    fs: `#version 300 es
        precision mediump float;
        in vec3 fragColor;
        out vec4 outColor;
     
        void main() {
            outColor = vec4(fragColor, 1);
        }`
};