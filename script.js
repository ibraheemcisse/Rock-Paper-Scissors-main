document.getElementById("play-btn").addEventListener("click", function() {
    const playerChoice = document.getElementById("choice").value
    const choices = ["Rock", "Paper", "Scissors"]
    const computerChoice = choices[Math.floor(Math.random() * choices.length)]
    let result = ""
  
    if (playerChoice === computerChoice) {
      result = "It's a tie!"
    } else if (
      (playerChoice === "Rock" && computerChoice === "Scissors") ||
      (playerChoice === "Paper" && computerChoice === "Rock") ||
      (playerChoice === "Scissors" && computerChoice === "Paper")
    ) {
      result = "You win!"
    } else {
      result = "Shame you lost to a computer AI will now become sentient!"
    }
  
    document.getElementById("player-choice").textContent = playerChoice
    document.getElementById("computer-choice").textContent = computerChoice
    document.getElementById("result").textContent = result
  })
  