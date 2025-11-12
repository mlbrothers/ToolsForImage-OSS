const { createFFmpeg, fetchFile } = FFmpeg;
const ffmpeg = createFFmpeg({ log: true });

document.getElementById('uploadForm').addEventListener('submit', async function(event) {
  event.preventDefault(); // Prevent the form from submitting the traditional way

  const imageFile = document.getElementById('image').files[0];
  const format = document.getElementById('format').value;
  const reader = new FileReader();

  reader.onload = async function() {
    if (!ffmpeg.isLoaded()) {
      await ffmpeg.load();
    }

    const data = new Uint8Array(reader.result);
    ffmpeg.FS('writeFile', 'input', data);
    await ffmpeg.run('-i', 'input', `output.${format}`);
    const output = ffmpeg.FS('readFile', `output.${format}`);

    const blob = new Blob([output.buffer], { type: `image/${format}` });
    const url = URL.createObjectURL(blob);
    const downloadLink = document.getElementById('downloadLink');
    downloadLink.href = url;
    downloadLink.download = `converted_image.${format}`;
    downloadLink.style.display = 'block';
    downloadLink.textContent = 'Download Converted Image';
  };

  reader.readAsArrayBuffer(imageFile);
});
