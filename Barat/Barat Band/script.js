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
    "594bb998-336c-47d4-8274-166b802ed71d.jpeg",
    "IMG_4098.jpeg",
    "IMG_4099.jpeg",
    "Picture7.jpg",
    "Picture8.jpg",
    "Picture9.jpg",
    "WhatsApp Image 2025-09-26 at 4.46.48 PM.jpeg",
    "WhatsApp Image 2025-09-26 at 4.46.49 PM.jpeg",
    "WhatsApp Image 2025-09-26 at 4.46.50 PM.jpeg",
    "WhatsApp Image 2025-09-26 at 4.46.51 PM.jpeg",
    "WhatsApp Image 2025-09-26 at 4.46.52 PM.jpeg",
    "WhatsApp Image 2025-09-26 at 4.46.53 PM.jpeg",
    "WhatsApp Image 2025-09-26 at 4.47.01 PM.jpeg",
    "WhatsApp Image 2025-09-26 at 4.47.03 PM.jpeg",
    "WhatsApp Image 2025-09-26 at 4.49.00 PM.jpeg",
    "1.mp4",
    "2.mp4",
    "3.mp4",
    "4.mp4",
    "5.mp4",
    "6.mp4",
    "7.mp4",
    "8.mp4",
    "9.mp4"
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
