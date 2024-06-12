<template>
    <div>
        <h2 class="text-center text-bold">Добро пожаловать в PsyNet</h2>
        <h5 class="text-center">Используйте наши передовые технологии для анализа социальных аккаунтов и выявления потенциальных психических расстройств у ваших пациентов.</h5>
    </div>
    <div class="q-pa-md row justify-center">
        <q-card class="q-pa-md col-7">
            <q-card-section horizontal row>
                <q-card-section class="text-h5 q-mt-md col-4" >
                    Методы анализа
                </q-card-section>
                <div class="row q-col-gutter-md">
                    <q-card v-for="info in infos" class="col-6 q-pa-sm" flat>
                        <q-card-section>
                            <q-icon :name="info.icon" color="primary" size="3rem" />
                            <div class="text-h6">{{ info.title }}</div>
                            <div class="text-subtitle2"> {{ info.subtitle }} </div>
                        </q-card-section>
                    </q-card>
                </div>
            </q-card-section>
        </q-card>
    </div>
  </template>
  
  <script setup>

    const infos = [
        {
            icon: "mdi-brain",
            title: "Анализ поведения",
            subtitle: "Используем передовые алгоритмы для анализа поведения пользователей в социальных сетях",
        },
        {
            icon: "mdi-stethoscope",
            title: "Идентификация симптомов",
            subtitle: "Помогаем выявлять симптомы психических расстройств на ранних стадиях",
        },
        {
            icon: "mdi-file-document-outline",
            title: "Персонализированные отчеты",
            subtitle: "Предоставляем подробные и персонализированные отчеты для медицинских профессионалов",
        },
        {
            icon: "mdi-lock-outline",
            title: "Конфиденциальность данных",
            subtitle: "Гарантируем полную конфиденциальность и безопасность данных",
        }
    ]
  </script>