create table "consoles" (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(55),
	"description" VARCHAR(512),
	"price" VARCHAR(25)
);

INSERT INTO "consoles" ("name", "description", "price")
VALUES ('Xbox Series X', 'The Xbox Series X has higher end hardware, and supports higher display resolutions - up to 8K resolution - along with higher frame rates and real-time ray tracing; it also has a high-speed solid-state drive to reduce loading times.', '$500 USD'), ('Xbox Series S', 'The less expensive Xbox Series S uses the same CPU, but has a less powerful GPU, has less memory and internal storage, and lacks an optical drive.', '$300 USD'), ('Playstation 5', 'The PlayStation 5s main hardware features include a solid-state drive customized for high-speed data streaming to enable significant improvements in storage performance, an AMD GPU capable of 4K resolution display at up to 120 frames per second, hardware-accelerated ray tracing for realistic lighting and reflections and the Tempest Engine allowing for hardware-accelerated 3D audio effects.', '$500 USD');
