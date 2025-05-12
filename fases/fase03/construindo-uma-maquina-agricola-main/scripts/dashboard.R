install.packages("ggplot2")

# Carregar pacotes
library(ggplot2)

# Carregar dados
dados <- read.csv("dados_irrigacao.csv")

# Converter timestamp para data
dados$timestamp <- as.POSIXct(dados$timestamp)

# Gráfico de Umidade
ggplot(dados, aes(x = timestamp, y = umidade)) +
    geom_line(color = "blue") +
    ggtitle("Nível de Umidade do Solo") +
    xlab("Tempo") +
    ylab("Umidade")

# Gráfico de pH
ggplot(dados, aes(x = timestamp, y = ph)) +
    geom_line(color = "green") +
    ggtitle("Nível de pH do Solo") +
    xlab("Tempo") +
    ylab("pH")
