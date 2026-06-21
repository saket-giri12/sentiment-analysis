async function translateText() {
  let text = document.getElementById("inputText").value;
  let from = document.getElementById("fromLang").value;
  let to = document.getElementById("toLang").value;

  if (!text) {
    alert("Please enter text");
    return;
  }

  try {
    let url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${from}&tl=${to}&dt=t&q=${encodeURIComponent(text)}`;

    let response = await fetch(url);
    let data = await response.json();

    let translated = data[0]
      .map(item => item[0])
      .join("");

    document.getElementById("outputText").value = translated;

  } catch (error) {
    console.error(error);
    alert("Translation failed");
  }
}