// script.js
function getFlagImage(country) {
  const flagMap = {
    "USA": "us.png",
    "France": "fr.png",
    "France/Netherlands": "fr.png",
    "Netherlands": "nl.png",
    "UK": "gb.png",
    "Germany": "de.png",
    "Italy": "it.png",
    "Japan": "jp.png",
    "Canada": "ca.png",
    "South Korea": "kr.png",
    "Israel": "il.png",
    "Brazil": "br.png",
    "Turkey": "tr.png",
    "India": "in.png",
    "Sweden": "se.png",
    "Spain": "es.png",
    "Switzerland": "ch.png",
    "Belgium": "be.png",
    "Singapore": "sg.png",
    "Norway": "no.png",
    "Taiwan": "tw.png",
    "China": "cn.png",
    "Austria": "at.png",
    // Add more as needed
    "": ""
  };
  return flagMap[country] || "";
}
// Fetch JSON
fetch('data.json')
  .then(response => response.json())
  .then(data => {
    const table = document.getElementById('data-table');

    // Create table header
    const header = table.createTHead();
    const headerRow = header.insertRow();
    const columns = ["Number","Company", "Country", "Revenue_nominal", "Revenue_abbrev"];
    columns.forEach(col => {
      const th = document.createElement('th');
      th.textContent = col.replace(/_/g, ' ');
      headerRow.appendChild(th);
    });

    // Create table body
    const tbody = table.createTBody();
    data.forEach(item => {
      const row = tbody.insertRow();
      columns.forEach(col => {
        const cell = row.insertCell();
        if (col === "Country") {
          const flagFile = getFlagImage(item[col]);
          if (flagFile) {
            const img = document.createElement('img');
            img.src = `h40/${flagFile}`;
            img.alt = item[col] + " flag";
            img.style.width = "24px";
            img.style.verticalAlign = "middle";
            img.style.marginRight = "0.5em";
            cell.appendChild(img);
          }
          cell.appendChild(document.createTextNode(item[col]));
        } else {
          cell.textContent = item[col];
        }
      });
    });
  })
  .catch(err => console.error('Error fetching JSON:', err));

  // 3. Fetch and render Markdown article (new)
document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("articles-container");

  fetch("map.md")   // adjust path if needed
    .then(response => response.text())
    .then(md => {
      const html = marked.parse(md);   // Markdown → HTML
      container.innerHTML = html;
    })
    .catch(err => console.error("Error loading article:", err));
});