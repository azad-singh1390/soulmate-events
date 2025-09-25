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
    "Big_1.jpeg",
    "Big_2.jpeg",
    "Big_3.jpeg",
    "Big_4.jpeg",
    "Big_5.jpeg",
    "Big_1.mp4",
    "Big_2.mp4",
    "Big_3.mp4",
    "Big_4.mp4"
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

    } else if (ext === "mp4") {
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
