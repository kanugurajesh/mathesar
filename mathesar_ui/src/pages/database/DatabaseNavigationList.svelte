<script lang="ts">
  import {
    Menu,
    LinkMenuItem,
    MenuHeading,
    Help,
  } from '@mathesar-component-library';
  import { databases } from '@mathesar/stores/databases';
  import {
    DATABASE_CONNECTION_ADD_URL,
    getDatabasePageUrl,
  } from '@mathesar/routes/urls';
  import DatabaseName from '@mathesar/components/DatabaseName.svelte';
  import type { Database } from '@mathesar/AppTypes';

  export let database: Database | undefined = undefined;
</script>

<div class="database-list">
  <Menu>
    <MenuHeading
      style="display:flex;align-items:center;margin-bottom:var(--size-super-ultra-small)"
    >
      <span class="title">All Databases ({$databases.data.length})</span>
      <span class="help">
        <Help>
          To add or remove databases, visit the
          <a href={DATABASE_CONNECTION_ADD_URL}> Add Database Connection </a>
          section of mathesar.
        </Help>
      </span>
    </MenuHeading>
    {#each $databases.data as db (db.name)}
      <LinkMenuItem
        href={getDatabasePageUrl(db.name)}
        class={database?.id === db.id ? 'active' : ''}
      >
        <DatabaseName database={db} iconHasBox />
      </LinkMenuItem>
    {:else}
      <span class="no-databases-found">No Databases Found</span>
    {/each}
  </Menu>
</div>

<style>
  .database-list {
    padding-top: var(--size-large);
    --min-width: 100%;
    --icon-color: var(--brand-500);
    --NameWithIcon__icon-opacity: 1;
    --Menu__item-border-radius: var(--border-radius-m);
    --Menu__item-hover-background: var(--sand-200);
    --Menu__item-active-background: var(--sand-300);
    --Menu__item-active-hover-background: var(--sand-300);
    --Menu__item-focus-outline-color: var(--sand-400);
  }
  .title {
    font-weight: 500;
  }
  .help {
    margin-left: auto;
  }
  .no-databases-found {
    padding: 0.2em 0.5em;
    color: var(--slate-500);
  }
</style>
