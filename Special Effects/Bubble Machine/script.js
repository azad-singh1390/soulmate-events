// scripts.js
document.querySelectorAll(".video-album video").forEach(video => {
    video.addEventListener("play", () => {
        if (video.requestFullscreen) {
            video.requestFullscreen();
        } else if (video.webkitEnterFullscreen) {  // iPad/iPhone Safari
            video.webkitEnterFullscreen();
        } else if (video.msRequestFullscreen) {
            video.msRequestFullscreen();
        }
    });
});

// List of album files
const albumFiles = [
    "Bubble_1.jpg",
    "56a99839-2bce-4aba-8d01-3b4cebc38d59.mov",
    "88c7401a-89eb-4ed9-89b8-c3c33a749d43.mov",
    "Bubble_1.mp4",
    "Bubble_2.mp4",
    "Bubble_3.mp4",
    "Bubble_4.mp4",
    "Bubble_5.mp4",
    "IMG_7237.MOV"
];

const album = document.getElementById("video-album");

albumFiles.forEach(file => {
    const ext = file.split(".").pop().toLowerCase();

    if (["jpg", "jpeg", "png", "gif"].includes(ext)) {
        // Create <img>
        const img = document.createElement("img");
        img.src = file;
        img.alt = "Haldi";
        img.className = "album-img"; // style in CSS instead of inline
        album.appendChild(img);

    } else if (ext === "mp4" || ext === "mov") {
        // Create <video>
        const video = document.createElement("video");
        video.controls = true;
        video.innerHTML = `<source src="${file}" type="video/mp4">
                           Your browser does not support the video tag.`;

        // Attach fullscreen event
        video.addEventListener("play", () => {
            if (video.requestFullscreen) {
                video.requestFullscreen();
            } else if (video.webkitEnterFullscreen) {  // iOS Safari
                video.webkitEnterFullscreen();
            } else if (video.msRequestFullscreen) {
                video.msRequestFullscreen();
            }
        });

        album.appendChild(video);

        // Create <a> download link
        const link = document.createElement("a");
        link.href = file;
        link.download = "";
        link.textContent = "Download";
        link.className = "download-link";
        album.appendChild(link);
    }
});
