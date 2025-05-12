# Dados das culturas em R
milho_dados <- list(
  sementes_por_hectare = 20,      # kg por hectare
  agua_por_hectare = 0.6,         # m³ por hectare
  herbicida_por_hectare = 3,      # litros por hectare
  inseticida_por_hectare = 0.5,   # litros por hectare
  fungicida_por_hectare = 1.5,    # litros por hectare
  calcario_por_hectare = 3.5,     # toneladas por hectare
  plantas_por_hectare = 60000,    # número de plantas por hectare
  produtividade_por_hectare = 8   # toneladas por hectare
)

cafe_dados <- list(
  mudas_por_hectare = 4000,       # mudas por hectare
  agua_por_hectare = 1.5,         # m³ por hectare
  herbicida_por_hectare = 2,      # litros por hectare
  inseticida_por_hectare = 1.5,   # litros por hectare
  fungicida_por_hectare = 3,      # litros por hectare
  calcario_por_hectare = 3.5,     # toneladas por hectare
  plantas_por_hectare = 8000,     # número de plantas por hectare
  produtividade_por_hectare = 25  # sacas por hectare
)

feijao_dados <- list(
  sementes_por_hectare = 60,      # kg por hectare
  agua_por_hectare = 0.5,         # m³ por hectare
  herbicida_por_hectare = 2,      # litros por hectare
  inseticida_por_hectare = 0.7,   # litros por hectare
  fungicida_por_hectare = 0.7,    # litros por hectare
  calcario_por_hectare = 3,       # toneladas por hectare
  plantas_por_hectare = 300000,   # número de plantas por hectare
  produtividade_por_hectare = 2   # toneladas por hectare
)

mandioca_dados <- list(
  manivas_por_hectare = 12000,    # manivas por hectare
  agua_por_hectare = 0.7,         # m³ por hectare
  herbicida_por_hectare = 3,      # litros por hectare
  inseticida_por_hectare = 1.5,   # litros por hectare
  fungicida_por_hectare = 1.5,    # litros por hectare
  calcario_por_hectare = 2,       # toneladas por hectare
  plantas_por_hectare = 12000,    # número de plantas por hectare
  produtividade_por_hectare = 25  # toneladas por hectare
)

# Função para calcular a média
calcular_media <- function(valores) {
  return(mean(valores))
}

# Função para calcular o desvio padrão
calcular_desvio_padrao <- function(valores) {
  return(sd(valores))
}

# Função para calcular estatísticas básicas (média e desvio padrão) com verificação
calcular_estatisticas <- function(consumos) {
  estatisticas <- list()
  
  # Verificar e calcular estatísticas para diferentes tipos de "sementes"
  if ("sementes_por_hectare" %in% names(consumos)) {
    estatisticas$media_sementes <- calcular_media(consumos$sementes_por_hectare)
    estatisticas$desvio_sementes <- calcular_desvio_padrao(consumos$sementes_por_hectare)
  } else if ("mudas_por_hectare" %in% names(consumos)) {
    estatisticas$media_sementes <- calcular_media(consumos$mudas_por_hectare)
    estatisticas$desvio_sementes <- calcular_desvio_padrao(consumos$mudas_por_hectare)
  } else if ("manivas_por_hectare" %in% names(consumos)) {
    estatisticas$media_sementes <- calcular_media(consumos$manivas_por_hectare)
    estatisticas$desvio_sementes <- calcular_desvio_padrao(consumos$manivas_por_hectare)
  } else {
    estatisticas$media_sementes <- NA
    estatisticas$desvio_sementes <- NA
  }
  
  # Continuar com os demais cálculos como estão
  if ("agua_por_hectare" %in% names(consumos)) {
    estatisticas$media_agua <- calcular_media(consumos$agua_por_hectare)
    estatisticas$desvio_agua <- calcular_desvio_padrao(consumos$agua_por_hectare)
  }
  
  if ("herbicida_por_hectare" %in% names(consumos)) {
    estatisticas$media_herbicida <- calcular_media(consumos$herbicida_por_hectare)
    estatisticas$desvio_herbicida <- calcular_desvio_padrao(consumos$herbicida_por_hectare)
  }
  
  if ("inseticida_por_hectare" %in% names(consumos)) {
    estatisticas$media_inseticida <- calcular_media(consumos$inseticida_por_hectare)
    estatisticas$desvio_inseticida <- calcular_desvio_padrao(consumos$inseticida_por_hectare)
  }
  
  if ("fungicida_por_hectare" %in% names(consumos)) {
    estatisticas$media_fungicida <- calcular_media(consumos$fungicida_por_hectare)
    estatisticas$desvio_fungicida <- calcular_desvio_padrao(consumos$fungicida_por_hectare)
  }
  
  if ("calcario_por_hectare" %in% names(consumos)) {
    estatisticas$media_calcario <- calcular_media(consumos$calcario_por_hectare)
    estatisticas$desvio_calcario <- calcular_desvio_padrao(consumos$calcario_por_hectare)
  }
  
  if ("plantas_por_hectare" %in% names(consumos)) {
    estatisticas$media_plantas <- calcular_media(consumos$plantas_por_hectare)
    estatisticas$desvio_plantas <- calcular_desvio_padrao(consumos$plantas_por_hectare)
  }
  
  if ("produtividade_por_hectare" %in% names(consumos)) {
    estatisticas$media_produtividade <- calcular_media(consumos$produtividade_por_hectare)
    estatisticas$desvio_produtividade <- calcular_desvio_padrao(consumos$produtividade_por_hectare)
  }
  
  return(estatisticas)
}

# Função para exibir resultados das estatísticas
exibir_estatisticas <- function(area, cultura, resultado) {
  cat("\nEstatísticas para", area, "hectares de", cultura, ":\n")
  cat("Média de sementes:", resultado$media_sementes, "\n")
  cat("Desvio padrão de sementes:", resultado$desvio_sementes, "\n")
  cat("Média de água:", resultado$media_agua, "\n")
  cat("Desvio padrão de água:", resultado$desvio_agua, "\n")
  cat("Média de herbicida:", resultado$media_herbicida, "\n")
  cat("Desvio padrão de herbicida:", resultado$desvio_herbicida, "\n")
  cat("Média de inseticida:", resultado$media_inseticida, "\n")
  cat("Desvio padrão de inseticida:", resultado$desvio_inseticida, "\n")
  cat("Média de fungicida:", resultado$media_fungicida, "\n")
  cat("Desvio padrão de fungicida:", resultado$desvio_fungicida, "\n")
  cat("Média de calcário:", resultado$media_calcario, "\n")
  cat("Desvio padrão de calcário:", resultado$desvio_calcario, "\n")
  cat("Média de plantas:", resultado$media_plantas, "\n")
  cat("Desvio padrão de plantas:", resultado$desvio_plantas, "\n")
  cat("Média de produtividade:", resultado$media_produtividade, "\n")
  cat("Desvio padrão de produtividade:", resultado$desvio_produtividade, "\n")
}

# Função para escolher a cultura
escolher_cultura <- function() {
  cat("Escolha uma cultura:\n")
  cat("1. Milho\n")
  cat("2. Café\n")
  cat("3. Feijão\n")
  cat("4. Mandioca\n")
  cat("5. Sair\n")
  
  escolha <- as.numeric(readline("Escolha uma opção: "))
  
#Add 15092024 - Verifica se primeira escolha é nula ("na" - not available)
  if (is.na(escolha)) {
    cat("Opção inválida. Tente novamente.\n")
    return(escolher_cultura())
  }
  
  if (escolha == 1) {
    return(list("Milho", milho_dados))
  } else if (escolha == 2) {
    return(list("Café", cafe_dados))
  } else if (escolha == 3) {
    return(list("Feijão", feijao_dados))
  } else if (escolha == 4) {
    return(list("Mandioca", mandioca_dados))
  } else if (escolha == 5) {
    return(list("Sair", NULL))
  } else {
    cat("Opção inválida. Tente novamente.\n")
    return(escolher_cultura())
  }
}

# Função para calcular os consumos para uma área específica
calcular_para_area <- function(area, dados) {
  consumos <- list()
  for (item in names(dados)) {
    consumos[[item]] <- dados[[item]] * area
  }
  return(consumos)
}

# Carregar as bibliotecas
library(httr)
library(jsonlite)

# Função para obter a previsão do tempo com ajuste no encoding
obter_previsao_tempo <- function() {
  url <- "http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/br?token=ef0476af7e8d0078b8d9f5dbd228e56e"
  
  # Fazer a requisição GET
  resposta <- GET(url)
  
  # Verificar se a requisição foi bem-sucedida
  if (status_code(resposta) == 200) {
    # Converter o conteúdo da resposta para JSON, ajustando o encoding para UTF-8
    conteudo <- fromJSON(content(resposta, as = "text", encoding = "UTF-8"))
    
    # Acessar o campo 'text' diretamente do data frame
    if (!is.null(conteudo$text)) {
      return(conteudo$text)
    } else {
      return("Previsão do tempo não disponível.")
    }
  } else {
    return("Erro ao obter a previsão do tempo.")
  }
}

# Função para exibir os cálculos e a previsão do tempo
exibir_resultados_e_previsao <- function(area, cultura, resultado) {
  # Exibir as estatísticas calculadas
  exibir_estatisticas(area, cultura, resultado)
  
  # Obter e exibir a previsão do tempo
  previsao <- obter_previsao_tempo()
  cat("\nAtenção: Prepare-se para o plantio nos próximos dias, de acordo com a previsão do tempo!", previsao, "\n")
}

# Função para atualizar dados de uma cultura
atualizar_dados <- function(cultura, dados) {
  while (TRUE) {
    cat(paste("\nAtualizando dados para", cultura, ":\n"))
    itens <- names(dados)
    for (i in seq_along(itens)) {
      cat(i, "-", itens[i], ":", dados[[itens[i]]], "\n")
    }
    cat(length(itens) + 1, "- Seguir sem atualizar\n")
    
    escolha <- as.integer(readline("Informe o número do item que deseja atualizar: "))
    if (!is.na(escolha) && escolha >= 1 && escolha <= length(itens)) {
      chave <- itens[escolha]
      novo_valor <- as.numeric(readline(paste("Informe o novo valor para", chave, ": ")))
      dados[[chave]] <- novo_valor
      cat(chave, "atualizado para", novo_valor, ".\n")
    } else if (escolha == length(itens) + 1) {
      cat("Seguindo sem atualizar.\n")
      break
    } else {
      cat("Número inválido.\n")
    }
    
    continuar <- toupper(readline("Deseja continuar atualizando dados? (S para Sim, N para Não): "))
    if (continuar != "S") {
      break
    }
  }
  return(dados)
}

# Função para deletar dados de uma cultura
deletar_dados <- function(cultura, dados) {
  while (TRUE) {
    cat(paste("\nDeletando dados para", cultura, ":\n"))
    itens <- names(dados)
    for (i in seq_along(itens)) {
      cat(i, "-", itens[i], ":", dados[[itens[i]]], "\n")
    }
    cat(length(itens) + 1, "- Seguir sem deletar\n")
    
    escolha <- as.integer(readline("Informe o número do item que deseja deletar: "))
    if (!is.na(escolha) && escolha >= 1 && escolha <= length(itens)) {
      chave <- itens[escolha]
      dados[[chave]] <- 0  # Define o valor como 0 ao invés de deletar a chave
      cat("Valor de", chave, "deletado (definido como 0).\n")
    } else if (escolha == length(itens) + 1) {
      cat("Seguindo sem deletar.\n")
      break
    } else {
      cat("Número inválido.\n")
    }
    
    continuar <- toupper(readline("Deseja continuar deletando dados? (S para Sim, N para Não): "))
    if (continuar != "S") {
      break
    }
  }
  return(dados)
}

# Função para exibir os dados no formato desejado
exibir_dados <- function(dados) {
  itens <- names(dados)
  for (i in seq_along(itens)) {
    cat(i, "-", itens[i], ":", dados[[itens[i]]], "\n")
  }
}

# Modifique o trecho onde os resultados são exibidos para incluir a previsão do tempo
menu_principal <- function() {
  while (TRUE) {
    # Escolha da primeira cultura
    cat("\n# Escolha a primeira cultura:\n")
    escolha1 <- escolher_cultura()
    cultura1 <- escolha1[[1]]
    dados1 <- escolha1[[2]]
    
    if (cultura1 == "Sair") {
      cat("Encerrando o programa...\n")
      break
    }
    
    # Verificação para garantir que a cultura seja válida
    if (is.null(dados1)) {
      next
    }
    
    # Perguntar a área para a primeira cultura
    area1 <- as.numeric(readline(paste("Informe a área para", cultura1, "(até 150 hectares): ")))
    if (is.na(area1) || area1 > 150 || area1 <= 0) {
      cat("Área inválida. Deve ser entre 1 e 150 hectares.\n")
      next
    }
    
    # Perguntar se o usuário quer escolher uma segunda cultura
    escolha_segunda_cultura <- toupper(readline("\nDeseja escolher uma segunda cultura? (S/N): "))
    
    if (escolha_segunda_cultura == "S") {
      # Segunda escolha de cultura
      cat("\n# Escolha a segunda cultura:\n")
      escolha2 <- escolher_cultura()
      cultura2 <- escolha2[[1]]
      dados2 <- escolha2[[2]]
      
      if (cultura2 == "Sair") {
        cat("Encerrando o programa...\n")
        break
      }
      
      # Verificação para garantir que a cultura seja válida
      if (is.null(dados2)) {
        next
      }
      
      # Perguntar a área para a segunda cultura
      area2 <- as.numeric(readline(paste("Informe a área para", cultura2, "(até 150 hectares): ")))
      if (is.na(area2) || area2 > 150 || area2 <= 0) {
        cat("Área inválida. Deve ser entre 1 e 150 hectares.\n")
        next
      }
    } else {
      cultura2 <- NULL
      area2 <- NULL
      dados2 <- NULL
    }
    
    # Calcular e exibir resultados para a primeira cultura
    cat("\nResultados para", area1, "hectares de", cultura1, ":\n")
    resultado1 <- calcular_para_area(area1, dados1)
    estatisticas1 <- calcular_estatisticas(resultado1)
    exibir_resultados_e_previsao(area1, cultura1, estatisticas1)
    
    # Calcular e exibir resultados para a segunda cultura (se houver)
    if (!is.null(cultura2)) {
      cat("\nResultados para", area2, "hectares de", cultura2, ":\n")
      resultado2 <- calcular_para_area(area2, dados2)
      estatisticas2 <- calcular_estatisticas(resultado2)
      exibir_resultados_e_previsao(area2, cultura2, estatisticas2)
    }

    # Perguntar se o usuário deseja atualizar dados de ambas as culturas
    atualizar <- readline("\nDeseja atualizar algum dado das culturas? (S para Sim, N para Não): ")
    if (toupper(atualizar) == "S") {
      # Atualizar dados da primeira cultura
      dados1 <- atualizar_dados(cultura1, dados1)
      
      # Atualizar dados da segunda cultura, se houver
      if (!is.null(cultura2)) {
        dados2 <- atualizar_dados(cultura2, dados2)
      }
    }
    
    # Perguntar se o usuário deseja deletar dados de ambas as culturas
    deletar <- readline("\nDeseja deletar algum dado das culturas? (S para Sim, N para Não): ")
    if (toupper(deletar) == "S") {
      # Deletar dados da primeira cultura
      dados1 <- deletar_dados(cultura1, dados1)
      
      # Deletar dados da segunda cultura, se houver
      if (!is.null(cultura2)) {
        dados2 <- deletar_dados(cultura2, dados2)
      }
    }

    # Exibir dados atualizados no formato desejado
    cat(paste("\nDados atualizados para", cultura1, ":\n"))
    exibir_dados(dados1)
    
    if (!is.null(cultura2)) {
      cat(paste("\nDados atualizados para", cultura2, ":\n"))
      exibir_dados(dados2)
    }
    
    # Perguntar se o usuário deseja sair ou reiniciar
    reiniciar <- toupper(readline("\nDeseja realizar outra operação? (S para Sim, N para Não): "))
    if (reiniciar == "N") {
      cat("Encerrando o programa...\n")
      break
    }
  }
}

# Executar o menu principal
menu_principal()
