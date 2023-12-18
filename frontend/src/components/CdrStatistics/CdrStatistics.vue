<template>
  <div>
    <h1>CDR Statistic</h1>
    <v-data-table
        :headers="headers"
        :items="cdrList"
        :items-per-page="itemsPerPage"
        :page="pagination.page"
        :total-items="totalItems"
        @update:page="updatePage"
      > 

      <template v-slot:item="{ item }">
        <tr>
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
      </template>
    </v-data-table>
  </div>
</template>

<script src="./CdrStatistics.js"></script>
