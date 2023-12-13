<template>
  <div>
    <h1>CDR Statistic</h1>
    <button @click="refreshData">Refresh Data</button>
    <table>
      <!-- Заголовки таблицы -->
      <thead>
        <tr>
          <th>ID</th>
          <th>Source</th>
          <th>Destination</th>
          <th>Start Time</th>
          <th>Answer Time</th>
          <th>End Time</th>
          <th>Duration (sec)</th>
          <th>Billable Seconds</th>
          <th>Disposition</th>
        </tr>
      </thead>
      <!-- Тело таблицы -->
      <tbody>
        <tr v-for="item in paginatedCdrList" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.src }}</td>
          <td>{{ item.dst }}</td>
          <td>{{ item.start }}</td>
          <td>{{ item.answer }}</td>
          <td>{{ item.end }}</td>
          <td>{{ item.duration }}</td>
          <td>{{ item.billsec }}</td>
          <td>{{ item.disposition }}</td>
        </tr>
      </tbody>
    </table>

    <!-- Пагинация -->
    <div class="pagination">
      <button @click="changePage(-1)" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="changePage(1)" :disabled="currentPage === totalPages">Next</button>
    </div>
  </div>
</template>

<script src="./CdrStatistics.js"></script>
<style scoped src="./CdrStatistics.css"></style>